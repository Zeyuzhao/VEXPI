#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO
import serial

win10_port = "COM2"
pi_port = "/dev/ttyAMA0"
serialPort = serial.Serial(pi_port, baudrate=115200, timeout=3.0)

async_mode = None

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

sensors = ['temp', 'light', "sal", 'wind']
def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        """Collect Data right here"""
        serialRaw = serialPort.readline()
        serialText = serialRaw.decode("utf-8").split(",")
        data = serialText.split(",")
        if len(data) == 4:
            output = {}
            for i in range(len(sensors)):
                output[sensors[i]] = data[i]
            count += 1
            print(output)
            socketio.emit('sensor',
                      output,
                      namespace='/test')
        socketio.sleep(0.2)

@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/css/epoch.min.css')
def epochCSS():
    return render_template('epoch.min.css')

@app.route('/script/epoch.min.js')
def epochJS():
    return render_template('epoch.min.js')


if __name__ == '__main__':
    socketio.run(app, debug=True)