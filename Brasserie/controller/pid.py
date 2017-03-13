#!/usr/bin/env python3

import numpy as np
from time import time

class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = list()
        self.integral_n = 10
        self.prev_time = 0
        self.target = 0

    def set_target(self, target):
        self.target = target


    def error(self, input):
        return input - self.target

    @property
    def dt(self):
        if self.prev_time == 0:
            self.prev_time = time()
            return 1
        dt = time() - self.prev_time
        self.prev_time = time()
        return dt

    def get_value(self, input):
        error = self.error(input)
        dt = self.dt
        p = self.proportinal(error)
        i = self.integrative(error, dt)
        d = self.derivative(error, dt)
        return p + i + d

    def proportinal(self, error):
        return self.kp*error

    def integrative(self, error, dt):
        value = self.ki*error*dt
        self.integral.append(value)
        if (len(self.integral) > 10):
            self.integral.pop(0)
        return np.sum(self.integral)

    def derivative(self, error, dt):
        return self.kd*(error-self.prev_error)/dt

