import wax
from flask import Flask, send_file
from timer import RepeatTimer, write_data_to_csv, wax_read
from flask_cors import CORS

app = Flask(__name__, static_folder=".")
plc = wax.connect()
timers = []

timer = RepeatTimer(1, lambda: write_data_to_csv(wax_read(plc)))
timer.start()

CORS(app)


@app.route("/")
def home():
    return "Nothing here"


@app.route("/unlock")
def unlock():
    print("Unlock called")
    wax.unlock(plc)
    return "OK"


@app.route("/begin")
def begin():
    global timer
    print("Begin called")
    timer.cancel()
    timer = RepeatTimer(0.1, lambda: write_data_to_csv(wax_read(plc)))
    timer.start()
    wax.begin(plc)
    return "OK"


@app.route("/end")
def end():
    global timer
    print("End called")
    timer.cancel()
    timer = RepeatTimer(1, lambda: write_data_to_csv(wax_read(plc)))
    timer.start()
    wax.end(plc)
    return "OK"


@app.route("/up")
def up():
    print("Up called")
    wax.up(plc)
    return "OK"


@app.route("/down")
def down():
    print("Down called")
    wax.down(plc)
    return "OK"


@app.route("/stop")
def stop():
    print("Stop called")
    wax.stop(plc)
    return "OK"


@app.route("/open")
def open():
    print("Open called")
    wax.open(plc)
    return "OK"


@app.route("/close")
def close():
    print("Close called")
    wax.close(plc)
    return "OK"


@app.route("/cancel")
def cancel():
    global timer
    timer.cancel()
    timer = RepeatTimer(1, lambda: write_data_to_csv(wax_read(plc)))
    timer.start()
    print("Cancel called")
    wax.cancel(plc)
    return "OK"


@app.route("/isfree")
def isfree():
    print("IsFree called")
    return wax.isFree(plc)


@app.route("/logs")
def logs():
    print("Logs called")
    return send_file("data.csv")
