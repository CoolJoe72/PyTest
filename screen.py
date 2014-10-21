#!/usr/bin/env python
# encoding: utf-8
"""
screen.py
this tests the pygame functions to display a number of screen graphics.
Created by Joseph on 2014-10-11.
Copyright (c) 2014 Gray Squared. All rights reserved.
"""

import sys, os
#from time import sleep
#import pygame
from platform import system, machine
if (system() == 'Linux' and machine() == 'armv6l'):
	import RPi.GPIO as GPIO
	
	change = 22
	end = 18
	blue = 23
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(blue,GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(change,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(end,GPIO.IN, pull_up_down=GPIO.PUD_UP)


def main():
	person = input('Enter your name: ')
	print('Hello', person)


def cleanup():
	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()

