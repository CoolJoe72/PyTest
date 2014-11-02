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
end = 18
i = 0

GPIO.setmode(GPIO.BOARD)
for pin in leds:
	GPIO.setup(pin, GPIO.OUT)

GPIO.setup(end, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
	global i
	while True:
		if not (GPIO.input(end)):
			cleanup()
		ledon(leds[i])
		sleep(.5)
		ledoff(leds[i])
		sleep(.5)
		i += 1

def ledon(pin):
	GPIO.output(pin,1)

def ledoff(pin):
	GPIO.output(pin,0)

def cleanup():
	print("end pushed")
	GPIO.cleanup()
	sys.exit()


if __name__ == "__main__":
   main()
