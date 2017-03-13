#!/usr/bin/env python3

from glob import glob
from threading import Thread, Event
import os
from time import sleep
from flask_socketio import SocketIO, emit


class Temp1W:
    def __init__(self, sensor_id=None):
        self.id = sensor_id if sensor_id is not None else self.get_first_id()
        self.file = os.path.join('/sys/bus/w1/devices/',self.id,'w1_slave')

    def read_raw(self):
        lines = list()
        with open(self.file, 'r') as f:
            lines =  f.readlines()
            f.close()
        return lines

    def read(self):
        lines = self.read_raw()
        eq = lines[1].find('=')
        if eq != -1:
            temp = float(lines[1][eq+1:-1])/1000
            return temp
        return None

    def get_first_id(self):
        return os.path.basename(glob('/sys/bus/w1/devices/28-*')[0])


