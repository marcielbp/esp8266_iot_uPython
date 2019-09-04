#Main.py
import network
import dht
from machine import Pin
import bme280
import urequests
sta_if = network.WLAN(network.STA_IF)
sta_if.connect('iPhone de Marciel', 'qazwsxqwe')
sta_if.isconnected()
sensor = dht.DHT11(Pin(14))
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)

while 1:
	sensor.measure()
	a =  'https://script.google.com/macros/s/AKfycbwOzbQdFGxL5_u-M4SRZWCHCMt-9XC07PXKNWxcyKIZu778Uio/exec?allData=blank-' + str(sensor.humidity()) + '-12-13-14'
	urequests.get(a)
	print(bme.values)
	print(sensor.humidity())
