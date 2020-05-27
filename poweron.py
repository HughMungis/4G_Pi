#!/usr/bin/python

import RPi.GPIO as GPIO
import serial
import time

ser = serial.Serial('/dev/ttyS0',115200)
ser.flushInput()

power_key = 6
rec_buff = ''

def power_on(power_key):
        print('Powering on... Please wait')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(power_key,GPIO.OUT)
        time.sleep(0.1)
        GPIO.output(power_key,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(power_key,GPIO.LOW)
        time.sleep(20)
        ser.flushInput()
        print('Done!')

try:
        power_on(power_key)

except:
        if ser != None:
                ser.close()
                GPIO.cleanup()

if ser != None:
                ser.close()
                GPIO.cleanup()
