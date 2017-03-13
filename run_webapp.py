#!/usr/bin/env python3

from flask import Flask, request, jsonify, render_template, url_for, send_from_directory
from flask_socketio import SocketIO, emit
from glob import glob
from threading import Thread, Event
import os
import json

from dev import ThreadTemp1W

asset_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/html')
app = Flask(__name__, template_folder=asset_path)
socketio = SocketIO(app)

thermo = Thread()


@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('connect', namespace='/connect')
def connect():
    emit("connected")
    if not thermo.isAlive():
        thermo = ThreadTemp1W()
        thermo.start()

if __name__ == "__main__":
    socketio.run(app, host="alarmpi")
