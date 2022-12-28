import logging
import snap7
import time
import threading as th
from threading import Timer
from datetime import datetime

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def readTemperature() :
    T = plc.read("VW1036")
    print (T)
    T = str(T)
    with open('logs.txt', 'a') as f :
        f.write(T)
        f.write('\n')

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
                currentDateTime = datetime.now()
                currentDateTime = str(currentDateTime)
                with open('logs.txt', 'a') as f:
                    f.write(currentDateTime)
                    f.write('\n')
                timer = RepeatTimer(0.1, readTemperature)
                timer.start()
            else :
                print ("machine not unlocked, unlock machine first")
        elif ctrl == "end" :
            if plc.read("V1105.0") :
                plc.write("V10.3", 1)
                plc.write("V10.3", 0)
                print ("Ready")
                timer.cancel()
                f.close()
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
            f.close()
        elif ctrl == "read" :
            T = plc.read("VW1036")
            print(T)
        elif ctrl == "exit" :
            exit = False
        else :
            print ("Unknown command")

else : logger.error("connection failed")
plc.disconnect()
logger.info("Disconnected")
plc.destroy()
