#!/usr/bin/env python3

import RPi.GPIO as gpio

class Switch:
    def __init__(self, pin):
        self.state = 0
        self.pin = pin
        gpio.setup(pin, gpio.OUT)
        gpio.output(self.pin, self.state)

    def toggle(self):
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0
        gpio.output(self.pin, self.state)

    def on(self):
        self.state = 1
        gpio.output(self.pin, self.state)

    def off(self):
        self.state = 0
        gpio.output(self.pin, self.state)