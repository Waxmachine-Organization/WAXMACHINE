from threading import Timer
from datetime import datetime
import csv


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


def write_data_to_csv(data):
    # Get current time

    # Open CSV file for writing
    with open("data.csv", "a", newline="") as csvfile:
        # Create a writer object
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())

        # Write header if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write data row
        writer.writerow(data)


def wax_read(plc):
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
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tempInt1": tempInt1,
        "tempInt2": tempInt2,
        "tempExt": tempExt,
        "pyrometer": pyrometer,
        "isopropanol": isopropanol,
        "stateTime": stateTime,
        "stateFree": stateFree
    }
    return data
