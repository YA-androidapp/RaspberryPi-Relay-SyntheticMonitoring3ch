#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

# required:
#   pip install RPi.GPIO

import requests
import RPi.GPIO as GPIO
import time


port1 = 26
port2 = 20
port3 = 21
TARGET_URL = 'http://httpbin.org/status/500'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(port1, GPIO.OUT)
GPIO.setup(port2, GPIO.OUT)
GPIO.setup(port3, GPIO.OUT)

GPIO.output(port1, GPIO.HIGH)
GPIO.output(port2, GPIO.HIGH)
GPIO.output(port3, GPIO.HIGH)

try:
    while 1:
        r = requests.get(TARGET_URL)

        if r.status_code >= 500:
            GPIO.output(port1, GPIO.LOW)
            GPIO.output(port2, GPIO.HIGH)
            GPIO.output(port3, GPIO.HIGH)
        elif r.status_code >= 400:
            GPIO.output(port1, GPIO.HIGH)
            GPIO.output(port2, GPIO.LOW)
            GPIO.output(port3, GPIO.HIGH)
        else:
            GPIO.output(port1, GPIO.HIGH)
            GPIO.output(port2, GPIO.HIGH)
            GPIO.output(port3, GPIO.LOW)
        time.sleep(10)
finally:
    GPIO.cleanup()
