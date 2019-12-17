# esp8266_iot_uPython
This repo contains data for using DHT and Pressure sensors in esp8266 running uPython

## How to install firmware?

Access [http://micropython.org/](http://micropython.org/) to download firmware and follow install guide.

## How to send and receive file ESP-8266?

REPL: Use [`picocom`](https://developer.ridgerun.com/wiki/index.php/Setting_up_Picocom_-_Ubuntu): `$ picocom /dev/ttyUSB0 -b115200`

Send file: Use [`ampy`](https://github.com/scientifichackers/ampy): `$ ampy --port /dev/ttyUSB0 put filename.py`

Remove files (REPL)
```>>> import os
>>> os.listdir()
['boot.py', 'port_config.py', 'data.txt']
>>> os.mkdir('dir')
>>> os.remove('data.txt')
```

TODO:
 - [ ] Integrate datalogger project;
 - [ ] Check display driver [pcd8544](https://github.com/mcauser/micropython-pcd8544);
