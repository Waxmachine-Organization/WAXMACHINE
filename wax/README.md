# Wax Machine Server

To run this you need Python, and you need to install these Python dependencies:

```bash
pip install flask flask_cors
```

then you can run the app using this command:

```bash
flask --app main run
```

## Files

- The PLC connect and instruction commands are defined in [wax.py](./wax.py).
- Timer class and the CSV logging functions are defined in [timer.py](./timer.py).
- The actual server that listens to commands coming from the WebApp are defined in [main.py](./main.py).
