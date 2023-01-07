import csv
import sys
csvfilename="test.csv"
with open(csvfilename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='"')
    for row in csv_reader:
        print(row)
