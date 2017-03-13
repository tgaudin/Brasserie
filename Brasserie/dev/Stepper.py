import RPi.GPIO as gpio
from time import sleep

class Stepper:
    def __init__(self, pin_stp, pin_dir):
        gpio.setmode(gpio.BCM)
        gpio.setup(pin_stp, gpio.OUT)
        gpio.setup(pin_dir, gpio.OUT)
        gpio.output(pin_stp, 0)
        gpio.output(pin_dir, 0)
        self.pin_stp = pin_stp
        self.pin_dir = pin_dir
        self.dir = True

    def rotate(self, stp, delay=0.005):
        for i in range(stp):
            sleep(delay/2.)
            gpio.output(self.pin_stp, 1)
            sleep(delay/2.)
            gpio.output(self.pin_stp, 0)

    def toggle_dir(self):
        self.dir = not self.dir
        gpio.output(self.pin_dir, self.dir)

    def __del__(self):
        gpio.cleanup()
