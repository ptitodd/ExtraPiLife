import os
from time import sleep
import random
from phue import Bridge

class Screamer:
	def __init__(self):

		# Set Phillips Hue bridge IP
		self.__bridge = Bridge('10.0.13.23')
		self.__bridge.connect()
		self.__bridge.get_api()

		# clear the screen of the mouse using unclutter
		os.system('unclutter &')

	def stimulate(self):
		# create some light scenes to be used for our bulbs HUE 0 is red, SAT defines saturation of colour 0 being white
		lightStrobeOn = {'tansitiontime' : 0, 'on' : True, 'bri' : 254, 'hue' : 0 , 'sat' : 0}
		lightStrobeOff = {'transitiontime' : 0, 'on' : False, 'bri' : 254, 'hue' : 0, 'sat' : 0}
		lightFadeRed = {'transitiontime': 15, 'on' : True, 'bri' : 254, 'hue' : 0, 'sat' : 254}
		lightDefault = {'transitiontime': 30, 'on' : True, 'bri' : 254, 'hue' : 14910, 'sat': 144}
		
		video = self.__selectVideo()
		os.system('omxplayer -b /home/pi/' + randomvideo + ' &')

		# strobe the light
		self.__bridge.set_light( [11,12,15], lightStrobeOff)
		sleep(0.1)
		self.__bridge.set_light( [11,12,15], lightStrobeOn)
		sleep(0.1)
		self.__bridge.set_light( [11,12,15], lightStrobeOff)
		sleep(0.1)
		self.__bridge.set_light( [11,12,15], lightStrobeOn)
		sleep(0.1)
		self.__bridge.set_light( [11,12,15], lightStrobeOff)
		sleep(0.1)
		self.__bridge.set_light( [11,12,15], lightStrobeOn)
		sleep(0.1)
		self.__bridge.set_light( [11,12,15], lightStrobeOff)
		sleep(0.1)
		self.__bridge.set_light( [11,12,15], lightStrobeOn)
		sleep(0.1)
		self.__bridge.set_light( [11,12,15], lightStrobeOff)
		sleep(0.1)
		self.__bridge.set_light( [11,12,15], lightStrobeOn)
		sleep(0.1)
		self.__bridge.set_light( [11,12,15], lightStrobeOff)
		sleep(0.1)
		self.__bridge.set_light( [11,12,15], lightStrobeOn)
		sleep(0.1)
		self.__bridge.set_light( [11,12,15], lightStrobeOff)

		# fade lights to red
		self.__bridge.set_light( [11,12,15] , lightFadeRed)

	def __selectVideo(self):
		# randomly select a startle video
		videos = ['Boo1.mp4', 'Boo2.mp4', 'Boo3.mp4', 'Boo4.mp4', 'Boo5.mp4']
		return random.choice(videos)
