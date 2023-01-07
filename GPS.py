import time
import serial
import pynmea2
import RPi.GPIO as gpio


gpio.setmode(gpio.BCM)

port = "/dev/serial0"

ser = serial.Serial(port,baudrate=9600,timeout=0.5)

while 1:
    try:
        data=ser.readline()
    except:
        print("loading")

    if (data[0:6]=='$GPGGA'):

        mag = pynmea2.parse(data)

        latval = msg.lat

        concatlat="lat: "+str(latval)
        print(concatval)

        longval=msg.lon
        concatlon= "lon: "+lonval
        print(concatlon)


            
