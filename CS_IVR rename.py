import os
import csv

with open('CS_IVR_NOTES.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        name = row[0] + '.wav'
        new = row[1] + '.wav'
        if os.path.exists(name):
            os.rename(name, new)
        else:
            print (name + " does not exist")
