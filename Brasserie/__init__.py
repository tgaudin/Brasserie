#!/usr/bin/env python3

from .main import PIDLoop, MotorThread
from . import wiring

import RPi.GPIO as gpio
gpio.setmode(wiring.MODE)