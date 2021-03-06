# esp8266_iot_uPython
This repo contains data for using DHT and Pressure sensors in esp8266 running uPython

## How to install firmware?

Access [http://micropython.org/](http://micropython.org/) to download firmware and follow install guide.

## How to send and receive file ESP-8266?

REPL: Use [`picocom`](https://developer.ridgerun.com/wiki/index.php/Setting_up_Picocom_-_Ubuntu): `$ picocom /dev/ttyUSB0 -b115200`

Send file: Use [`ampy`](https://github.com/scientifichackers/ampy): `$ ampy --port /dev/ttyUSB0 put filename.py`

Remove files (REPL)
```
>>> import os
>>> os.listdir()
['boot.py', 'port_config.py', 'data.txt']
>>> os.mkdir('dir')
>>> os.remove('data.txt')
```

TODO:
 - [ ] Integrate datalogger project;
 - [ ] Check display driver [pcd8544](https://github.com/mcauser/micropython-pcd8544);
 
DOING:

- [x] Display driver [st7735](https://github.com/marcielbp/micropython-st7735-esp8266);
 
 ## Pinout ESP-8266-12E
 
 ![image](assets/images/ESP8266-NodeMCU-kit-12-E-pinout-gpio-pin.png)

## Pinout WEMOS-D1

![image](assets/images/ESP8266-WeMos-D1-Mini-pinout-gpio-pin.png)
