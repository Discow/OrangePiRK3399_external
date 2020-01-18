import time
import sys

import OPi.GPIO as GPIO

import orangepi.pi4
BOARD = orangepi.pi4.BOARD
GPIO.setmode(BOARD)

pin=int(sys.argv[1])

GPIO.setup(pin, GPIO.OUT)
while True:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(1)
