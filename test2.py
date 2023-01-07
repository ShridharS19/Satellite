import csv
import sys
import serial
import time
csvfilename="test.csv"
ser= serial.Serial(port='/dev/ttyAMA0',baudrate=9600)
with open(csvfilename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='"')
    for row in csv_reader:
        for cell in row:
            ser.write(str(cell).encode())
            ser.write(('\r\n').encode())
    

