#!/usr/bin/python

import RPi.GPIO as GPIO
import serial
import time

ser = serial.Serial('/dev/ttyS0',115200)
ser.flushInput()

power_key = 6
rec_buff = ''

def power_on(power_key):
        print('Reinitializing stuff...')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(power_key,GPIO.OUT)
        time.sleep(0.1)
        GPIO.output(power_key,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(power_key,GPIO.LOW)
        time.sleep(20)
        ser.flushInput()
        print('Step 1 complete...')

def power_down(power_key):
        print('Gracefully powering the PiHat down...')
        GPIO.output(power_key,GPIO.HIGH)
        time.sleep(3)
        GPIO.output(power_key,GPIO.LOW)
        time.sleep(18)
        print('Done!')

def send_at(command,back,timeout):
        rec_buff = ''
        ser.write((command+'\r\n').encode())
        time.sleep(timeout)
        if ser.inWaiting():
                time.sleep(0.1 )
                rec_buff = ser.read(ser.inWaiting())
        if rec_buff != '':
                if back not in rec_buff.decode():
                        print(command + ' ERROR')
                        print(command + ' back:\t' + rec_buff.decode())
                        return 0
                else:
                        print(rec_buff.decode())
                        return 1
        else:
                print(command + ' no responce')

try:
        power_on(power_key)
        power_down(power_key)
except:
        if ser != None:
                ser.close()
                GPIO.cleanup()

if ser != None:
                ser.close()
                GPIO.cleanup()
