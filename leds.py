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
end = 18
i = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(bgreen, GPIO.OUT)
GPIO.setup(bwhite, GPIO.OUT)
blue_on, blue_off = GPIO.output(blue,1),GPIO.output(blue,0)
red_on, red_off = GPIO.output(red,1),GPIO.output(red,0)
green_on, green_off = GPIO.output(green,1),GPIO.output(green,0)
bgreen_on, bgreen_off = GPIO.output(bgreen,1),GPIO.output(bgreen,0)
bwhite_on, bwhite_off = GPIO.output(bwhite,1),GPIO.output(bwhite,0)
GPIO.setup(end, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
	global i
	while True:
		if not (GPIO.input(end)):
			cleanup()
		blue_on
		sleep(.25)
		blue_off
		sleep(.25)

def cleanup():
	print("end pushed")
	GPIO.cleanup()
	sys.exit()


if __name__ == "__main__":
   main()