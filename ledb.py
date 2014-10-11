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
led = (blue, red, green, bgreen, bwhite)
ledn = ("Blue","Red","Green","Bright Green","Bright White")
change = 22
end = 18
i = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(bgreen, GPIO.OUT)
GPIO.setup(bwhite, GPIO.OUT)
GPIO.setup(change, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(end, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
	global i
	while True:
		if not (GPIO.input(change)):
			change_led()
		if not (GPIO.input(end)):
			cleanup()
		GPIO.output(led[i], 1)
		sleep(.25)
		GPIO.output(led[i], 0)
		sleep(.25)

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