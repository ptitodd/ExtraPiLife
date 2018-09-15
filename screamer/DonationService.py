from http.client import HTTPSConnection
from http import HTTPStatus
import json
import time

class DonationService:
	def __init__(self, baseUri, resource, onUpdateHandler):
		self.__httpConnection = HTTPSConnection(baseUri)
		self.__resource = resource
		self.__onUpdateHandler = onUpdateHandler
		self.__httpConnection.request("GET", self.__resource)
		response = self.__httpConnection.getresponse()
		self.__etag = response.getheader('ETag')
		response.read()

		self.__isDebug = False

	def start(self):
		while True:
			time.sleep(15) # ExtraLife / Donor Drive want request recurrences limited to 15 seconds
			self.__update()

	def startDebug(self):
		self.__isDebug = True
		self.start()

	def __update(self):
		header = {'If-none-match': self.__etag}
		self.__httpConnection.request("GET", self.__resource, headers=header)
		response = self.__httpConnection.getresponse()
		response.read()

		if (response.status == HTTPStatus.OK):
			self.__etag = response.getheader("ETag")
			self.__onUpdateHandler.stimulate()
		elif (self.__isDebug and response.status == HTTPStatus.NOT_MODIFIED):
			self.__onUpdateHandler.stimulate()

	