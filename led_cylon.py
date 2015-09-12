#!/usr/bin/env python
# This is based on the led_blink.py example that came with the GoPiGo
# to blink the LEDs

from gopigo import *
import sys
import time
import argparse

argparser = argparse.ArgumentParser(description='Script to activate GoPiGo LEDs in Cylon visor fashion.')
argparser.add_argument("-s","--speed", type=int, help="A number between 1 and 10 to choose the speed of LED on and off action. 1 is fastest, 10 is slowest.")
args = argparser.parse_args()

# default speed
speed = 5

if 1 <= args.speed <= 10: 
    speed = args.speed
        
delay = .01*speed*speed

# We wrap the loop with try/except in order to make sure that we turn off the
# LEDs when the script is interrupted with ctrl-c

try:
    while True:
        print ".",
        led_on(LED_L)
        time.sleep(delay)
        led_on(LED_R)
        time.sleep(delay)
        print "."
        led_off(LED_L)
        time.sleep(delay)
        led_off(LED_R)
        time.sleep(delay)


        print ".",
        led_on(LED_R)
        time.sleep(delay)
        led_on(LED_L)
        time.sleep(delay)
        print "."
        led_off(LED_R)
        time.sleep(delay)
        led_off(LED_L)
        time.sleep(.5)
except KeyboardInterrupt:
    print "Turning off LEDs and shutting down..."
    led_off(LED_L)
    led_off(LED_R)
    raise SystemExit
                        
    
