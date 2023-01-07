import serial
import time
ser= serial.Serial(port='/dev/ttyAMA0',baudrate=9600)
idx=0
while True:
    ser.write(str(idx).encode())
    ser.write(('\r\n').encode())
    time.sleep(1)
    idx+=1
