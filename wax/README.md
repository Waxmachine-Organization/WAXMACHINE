# Wax Machine Server
Connect the Raspberry Pi to a Wifi network available on the locaiton of the machine. We can then access it through SSH protocol.

The first thing is to configure the Raspberry Pi as our server.
We need to set up the ip adress of the Siemens LOGO! PLC as 192.168.200.3.
We connect the the Raspberry Pi to our ethernet subnet on the interface eth0.

To run this you need Python, and you need to install these Python dependencies:

```bash
pip install flask flask_cors
```
You also need to add these dependencies :
- snap7
- timer

To install snap 7, you can run the following commands after compiling from the file in the repo:
```bash
pip3 install python-snap7
```

When installing these dependencies, we don't want to use a venv. If you need to force installing, we can use the pip option --break-system-packages

```bash
cd snap7-full-1.4.2
cd build/unix
sudo make -f arm_v7_linux.mk all
sudo make -f arm_v7_linux.mk install
pip3 install python-snap7 --break-system-packages
```
Note: This version of arm_v7_linux has been modified to be:
```bash
##
## ARMHF V7 tested on 
## - pcDUINO board - UBUNTU based
## - BeagleBone Black - Angstrom based
## - Cubieboard 2 - Debian based
##
## To improve the build speed in small systems disable -pedantic
## switch in CXXFLAGS
##
TargetCPU  :=arm_v7
OS         :=linux
CXXFLAGS   := -O3 -g -fPIC -pedantic #Modified Line

# Standard part

include common.mk
```
Both Flask and ngrok need to be added to the path and should follow this dependencies :
```bash
module.exports = {
  apps: [
    {
      name: "Flask",
      args: "--app main run",
      cwd: "/home/admin/wax-server/wax",
      script: "/usr/local/bin/flask",
      env: {},
      exec_interpreter: "none",
      },
    {
      name: "Ngrok",
      args: "http --hostname=wax.eu.ngrok.io 5000",
      cwd: "/home/admin/wax-server",
      script: "/usr/local/bin/ngrok",
      env: {},
    },
  ],
};
```


We also need to install ngrok on the Raspberry Pi, using the commands and the token in their website.
```bash
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
```
```bash
ngrok config add-authtoken 2HwzeiqtqAtanwUiNRnMgCFCtU0_3fWSdMBPnrtsniTjqBpA4
```
Then you need to open the dhcpcd.conf file and add the following lines

```bash
interface eth0
static ip_address=192.168.200.4/24
static routers=000.000.000.000
static domain_name_servers=255.255.255.0


interface wlan0
static ip_address=192.168.101.82 //change this to the network you're connected to.
static routers=192.168.101.1
```

Then add this to the .bashrc file (to do, not sure if needed):
```bash
disable eth0
wait 10 seconds
pm2 restart 0
wait 10 sec
enable eth0
```

then you can run the app using this command:

```bash
flask --app main run
```

The difefrent processes (Flask and Ngrok) are managed through pm2. When in this repo, we can use the following :
To install npm, we can use (required node):
```bash
npm install pm2
```


```bash
pm2 start
```

```bash
pm2 restart 0
```

```bash
pm2 stop all
```

```bash
pm2 status
```

```bash
pm2 logs
```

## Files

- The PLC connect and instruction commands are defined in [wax.py](./wax.py).
- Timer class and the CSV logging functions are defined in [timer.py](./timer.py).
- The actual server that listens to commands coming from the WebApp are defined in [main.py](./main.py).

