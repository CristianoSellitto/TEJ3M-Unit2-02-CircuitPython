# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""Example for Pico. Blinks the built-in LED."""
import time
import board
import digitalio

blink_time = 1   # set blink_time to 1
led = digitalio.DigitalInOut(board.LED)   # set the built-in LED to led
led.direction = digitalio.Direction.OUTPUT   # set the led direction to OUTPUT

while True:
    led.value = True        # turn built-in LED on
    time.sleep(blink_time)  # wait for the length of blink_time
    led.value = False       # turn built-in LED off
    time.sleep(1)           # wait a second
    
    blink_time = blink_time + 1 # add a second to blink_time
