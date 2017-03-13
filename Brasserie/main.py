#!/usr/bin/env

from .dev import Temp1W, Switch, Stepper
from .controller import PID
from . import wiring

from time import sleep
from threading import Thread
import logging

class PIDLoop(Thread):
    def __init__(self, delay=1.5, logger=None):
        self.pid = PID(wiring.PID_KP, wiring.PID_KI, wiring.PID_KD)
        self.ssr = Switch(wiring.PIN_SSR)
        self.t1 = Temp1W(wiring.THERMO_ID1)
        self.delay = delay
        self.logger = logger or logging.getLogger(__name__)
        super(PIDLoop, self).__init__()

    def set_target(self, target):
        self.pid.set_target(target)

    def run(self):
        while True:
            T =  self.t1.read()
            val = self.pid.get_value(T)
            if (val < 0):
                self.ssr.on()
            else:
                self.ssr.off()
            self.logger.info("T={}, PID={}".format(T, val))
            sleep(self.delay)

class MotorThread(Thread):
    def __init__(self, logger=None):
        self.motor = Stepper(wiring.PIN_MOTOR_STEP, wiring.PIN_MOTOR_DIR)
        self.state = True
        self.logger = logger or logging.getLogger(__name__)
        super(MotorThread, self).__init__()

    def run(self):
        logger.info("Starting motor")
        while self.state:
            self.motor.rotate(100)

    def pause(self):
        self.state = False

    def resume(self):
        self.state = True


