import logging
import snap7
import time
import csv
import threading as th
from threading import Timer
from datetime import datetime

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def write_data_to_csv(data):
    # Get current time
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Open CSV file for writing
    with open("data.csv", "a", newline="") as csvfile:
        # Create a writer object
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())

        # Write header if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write data row
        writer.writerow({**data, **{"timestamp": timestamp}})
    
def wax_read() :
    tempInt1 = plc.read("VW1036")
    #tempInt1 = str(tempInt1)
    tempInt2 = plc.read("VW1038")
    #tempInt2 = str(tempInt2)
    tempExt = plc.read("VW1032")
    #tempExt = str (tempExt)
    pyrometer = plc.read("VW1040")
    #pyrometer = str (pyrometer)
    isopropanol = plc.read("VW1042")
    #isopropanol = str(isopropanol)
    stateTime = plc.read("V1104.2")
    #stateTime = str (stateTime)
    stateFree = plc.read("V1104.3")
    #stateFree = str (stateFree)
    data = {
        "tempInt1": tempInt1,
        "tempInt2": tempInt2,
        "tempExt": tempExt,
        "pyrometer": pyrometer,
        "isopropanol": isopropanol,
        "stateTime": stateTime,
        "stateFree": stateFree
    }
    return data


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

plc = snap7.logo.Logo()
plc.connect("192.168.200.3", 0x2000, 0x2000)
logger.info("connected")
print (plc.get_connected())
exit = True
d = 435
if plc.get_connected():
    logger.info("connected")
    while exit :
        ctrl = input("Enter command:")
        if ctrl == "unlock" :
            if plc.read("V1104.2") :
                plc.write("V10.1", 1)
                plc.write("V10.1", 0)
                print ("Door unlocked, place skis, enter begin")
            else :
                print ("Machine not ready for use")
        elif ctrl == "begin" :
            if plc.read("V1104.3") :
                plc.write("V10.2", 1)
                plc.write("V10.2", 0)
                print ("Process starting")
                timer.cancel()
                timer = RepeatTimer(0.1, write_data_to_csv(wax_read))
                timer.start()
            else :
                print ("machine not unlocked, unlock machine first")
        elif ctrl == "end" :
            if plc.read("V1105.0") :
                plc.write("V10.3", 1)
                plc.write("V10.3", 0)
                print ("Ready")
                timer.cancel()
                timer = RepeatTimer(1, write_data_to_csv(wax_read))
                timer.start()
            else :
                print ("Process is not finished")
        elif ctrl == "up" :
            plc.write("V10.6", 0)
            plc.write("V10.5", 1)
        elif ctrl == "down" :
            plc.write("V10.5", 0)
            plc.write("V10.6", 1)
        elif ctrl == "stop" :
            plc.write("V10.5", 0)
            plc.write("V10.6", 0)
        elif ctrl == "open" :
            plc.write("V10.7", 1)
            plc.write("V10.7", 0)
        elif ctrl == "close" :
            plc.write("V10.0", 1)
            plc.write("V10.0", 0)
        elif ctrl == "cancel" :
            plc.write("V10.4", 1)
            plc.write("V10.4", 0)
            timer.cancel()
            timer = RepeatTimer(1, write_data_to_csv(wax_read))
            timer.start()
        elif ctrl == "read" :
            T = plc.read("VW1036")
            print(T)
        elif ctrl == "exit" :
            exit = False
        elif plc.read("V1104.2") :
            timer.cancel()
            timer = RepeatTimer(1, write_data_to_csv(wax_read))  #cette partie la elle pue la merde, a reprendre
            timer.start()
        else :
            print ("Unknown command")
else : logger.error("connection failed")
plc.disconnect()
logger.info("Disconnected")
plc.destroy()
