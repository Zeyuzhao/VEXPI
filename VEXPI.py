import time
from flask import Flask, jsonify, render_template
from multiprocessing import Process, Value

app = Flask(__name__)


@app.route("/control")
def home():
    return render_template('main.html', data=data)

def record_loop(loop_on):
   while True:
      if loop_on.value == True:
         print("loop running")
      time.sleep(1)

def readUART():
    return "hi"


if __name__ == "__main__":
    recording_on = Value('b', True)
    p = Process(target=record_loop, args=(recording_on,))
    p.start()
    app.run(host='0.0.0.0', port=80,use_reloader=False)
    p.join()
