from screamer import DonationService
from screamer import DonationPrinter
from screamer import Screamer

import sys

if __name__ == "__main__":

	isDebug = "--debug" in sys.argv

	handler = Screamer() if 'screamer' in sys.argv else DonationPrinter()

	# using the teams endpoints instead of the donor endpoint because if we get
	# over 100 donations then we have to deal with pagination. However, each
	# donation will change the team object numDonations and sumDonations so the
	# event will fire all the same.
	service = DonationService("www.extra-life.org", "/api/teams/38776", handler)
	if (isDebug):
		service.startDebug()
	else:
		service.start()

def usage():
	print("python test.py [printer|screamer] [--debug]")