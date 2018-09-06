import os
from time import sleep
import random
import RPi.GPIO as GPIO
from phue import Bridge

# Set Pi's GPIO to be used
GPIO.setmode(GPIO.BCM)

# Set Pin 6 to be ground, Set pin 12 to be 3.3v and use internal low/high resistor
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set Phillips Hue bridge IP
b = Bridge('10.0.13.23')

# Let's register our lights if we haven't done so
b.connect()

b.get_api()

# It's time to create some light scenes to be used for our bulbs HUE 0  is red, SAT defines saturation of colour 0 being white of course

lightStrobeOn = {'tansitiontime' : 0, 'on' : True, 'bri' : 254, 'hue' : 0 , 'sat' : 0}
lightStrobeOff = {'transitiontime' : 0, 'on' : False, 'bri' : 254, 'hue' : 0, 'sat' : 0}
lightFadeRed = {'transitiontime': 15, 'on' : True, 'bri' : 254, 'hue' : 0, 'sat' : 254}
lightDefault = {'transitiontime': 30, 'on' : True, 'bri' : 254, 'hue' : 14910, 'sat': 144}

# let's clear the screen of the mouse using unclutter
os.system('unclutter &')

# i used to ensure the status of our mat holds
i=0

while True:
	input_state = GPIO.input(18)

	# If someone is standing on the mat, so 3.3v suddenly becomes 0v as the charge crosses the metal contacts in our pressure plate
	if i == 0 and input_state == False:
		
		# let's randomly select a startle video
		videos = ['Boo1.mp4', 'Boo2.mp4', 'Boo3.mp4', 'Boo4.mp4', 'Boo5.mp4']
		randomvideo = random.choice(videos)
		os.system('omxplayer -b /home/pi/' + randomvideo + ' &')

		# now let's light it up
		# let's strobe the light 5 times
		b.set_light( [11,12,15], lightStrobeOff)
		sleep(0.1)
		b.set_light( [11,12,15], lightStrobeOn)
		sleep(0.1)
		b.set_light( [11,12,15], lightStrobeOff)
		sleep(0.1)
		b.set_light( [11,12,15], lightStrobeOn)
		sleep(0.1)
		b.set_light( [11,12,15], lightStrobeOff)
		sleep(0.1)
		b.set_light( [11,12,15], lightStrobeOn)
		sleep(0.1)
		b.set_light( [11,12,15], lightStrobeOff)
		sleep(0.1)
		b.set_light( [11,12,15], lightStrobeOn)
		sleep(0.1)
		b.set_light( [11,12,15], lightStrobeOff)
		sleep(0.1)
		b.set_light( [11,12,15], lightStrobeOn)
		sleep(0.1)
		b.set_light( [11,12,15], lightStrobeOff)
		sleep(0.1)
		b.set_light( [11,12,15], lightStrobeOn)
		sleep(0.1)
		b.set_light( [11,12,15], lightStrobeOff)

		# let's fade lights to red
		b.set_light( [11,12,15] , lightFadeRed)
		# set our hold switch on to avoid repeating the playback
		i = 1
		
		sleep(10)
	elif i == 1 and input_state == False:
		# likely unnecessary but lets just make sure that as long as the matt is pressed i remains as 1
		i = 1
	elif i == 1 and input_state == True:
		# until finally someone steps off the mat, then i can be 0 and the script is reset to trigger all the animations again
		b.set_light( [11,12,15], lightDefault)
		i = 0	
	
	sleep(0.1);
