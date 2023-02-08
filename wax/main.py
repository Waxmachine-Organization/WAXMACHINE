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
    wax.unlock(plc)
    return "OK"


@app.route("/begin")
def begin():
    wax.begin(plc)
    return "OK"


@app.route("/end")
def end():
    wax.end(plc)
    return "OK"


@app.route("/up")
def up():
    wax.up(plc)
    return "OK"


@app.route("/down")
def down():
    wax.down(plc)
    return "OK"


@app.route("/stop")
def stop():
    wax.stop(plc)
    return "OK"


@app.route("/open")
def open():
    wax.open(plc)
    return "OK"


@app.route("/close")
def close():
    wax.close(plc)
    return "OK"


@app.route("/cancel")
def cancel():
    wax.cancel(plc)
    return "OK"


@app.route("/isfree")
def isfree():
    return wax.isFree(plc)


@app.route("/istimefree")
def isTimeFree():
    return wax.isTimeFree(plc)


@app.route("/readisopropanol")
def readIsopropanol():
    return wax.readIsopropanol(plc)


@app.route("/readinttemp")
def readIntTemp():
    return wax.readIntTemp(plc)


@app.route("/readexttemp")
def readExtTemp():
    return wax.readExtTemp(plc)


@app.route("/readpyro")
def readPyro():
    return wax.readPyro(plc)


@app.route("/logs")
def logs():
    return send_file("data.csv")
