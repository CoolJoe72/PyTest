#!/usr/bin/python
# LED and Buton test ledb.py

import sys
import RPi.GPIO as GPIO
from time import sleep

blue = 23
red = 21
green = 19
bgreen = 15
bwhite = 13
leds = (blue, red, green, bgreen, bwhite)
ledn = ("Blue","Red","Green","Bright Green","Bright White")
change = 22
end = 18
i = 0

GPIO.setmode(GPIO.BOARD)
for pin in leds:
	GPIO.setup(pin, GPIO.OUT)

GPIO.setup(change, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(end, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
	global i
	while True:
		if not (GPIO.input(change)):
			change_led()
		if not (GPIO.input(end)):
			cleanup()
		ledon(led[i])
		sleep(.25)
		ledoff(led[i])
		sleep(.25)

def ledon(pin):
	GPIO.output(pin, 1)

def ledoff(pin):
	GPIO.output(pin, 0)

def change_led():
	global i
	print "Change button was pushed"
	i=i+1
	if i == len(led):
		i = 0
	print "Color is now" , ledn[i] 

def cleanup():
	print("end pushed")
	GPIO.cleanup()
	sys.exit()

if __name__ == "__main__":
   main()
