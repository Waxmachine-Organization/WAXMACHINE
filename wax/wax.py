import snap7


def connect():
    plc = snap7.logo.Logo()
    plc.connect("192.168.200.3", 0x2000, 0x2000)
    return plc


def unlock(plc):
    # if plc.read("V1104.2"):
    plc.write("V10.1", 1)
    plc.write("V10.1", 0)


def isFree(plc):
    return plc.read("V1104.3")


def isTimeFree(plc):
    return plc.read("V1104.2")


def readIsopropanol(plc):
    return plc.read("VW1042")


def readIntTemp(plc):
    return (plc.read("VW1036")+plc.read("VW1038"))/2


def readExtTemp(plc):
    return plc.read("VW1032")


def readPyro(plc):
    return plc.read("VW1042")
    

def begin(plc):
    # if plc.read("V1104.3"):
    plc.write("V10.2", 1)
    plc.write("V10.2", 0)


def end(plc):
    # if plc.read("V1105.0"):
    plc.write("V10.3", 1)
    plc.write("V10.3", 0)


def up(plc):
    plc.write("V10.6", 0)
    plc.write("V10.5", 1)


def down(plc):
    plc.write("V10.5", 0)
    plc.write("V10.6", 1)


def stop(plc):
    plc.write("V10.5", 0)
    plc.write("V10.6", 0)


def open(plc):
    plc.write("V10.7", 1)
    plc.write("V10.7", 0)


def close(plc):
    plc.write("V10.0", 1)
    plc.write("V10.0", 0)


def cancel(plc):
    plc.write("V10.4", 1)
    plc.write("V10.4", 0)


def destroy(plc):
    plc.disconnect()
    plc.destroy()


def reset(plc):
    plc.write("V11.1", 1)
    plc.write("V11.1", 0)
