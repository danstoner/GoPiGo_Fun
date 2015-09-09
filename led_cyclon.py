#!/usr/bin/env python
# This is based on the led_blink.py example that came with the GoPiGo
# to blink the LEDs

## TODO:
## 1. add command-line parameter to control blink speed
## 2. catch exceptions to make sure we are turning off LEDs at
###   program termination (rather than leaving them in last on/off state)

from gopigo import *
import sys
import time

while True:
    print "."
    led_on(LED_L)
    time.sleep(.5)
    led_on(LED_R)
    time.sleep(.5)
    print "."
    led_off(LED_L)
    time.sleep(.5)
    led_off(LED_R)
    time.sleep(.5)


    print "."
    led_on(LED_R)
    time.sleep(.5)
    led_on(LED_L)
    time.sleep(.5)
    print "."
    led_off(LED_R)
    time.sleep(.5)
    led_off(LED_L)
    time.sleep(.5)

    
