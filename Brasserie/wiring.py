#!/usr/bin/env python

import RPi.GPIO as gpio

MODE        = gpio.BCM
PIN_MOTOR_STEP  = 23
PIN_MOTOR_DIR   = 18 
PIN_SSR         = 21

THERMO_ID1 = "28-000005f0e318"
THERMO_ID2 = "28-00000801df5e"

PID_KP = 200.0
PID_KI = 15.0
PID_KD = 20.0
