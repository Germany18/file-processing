import os
import csv
path = input ("Please enter directory ")
file = input ("Enter file name ")
fullPath = f"{path}/{file}.csv"
name = input ("Enter name ")
address = input ("Enter address ")
phone = input ("Enter phone ")
checkFolder = os.path.isdir(path)
def writetofile (fullPath, name, address, phone):
    with open( fullPath, 'w+', newline='') as csvfile:
        fieldnames = ['name', 'address', 'phone']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'name': name, 'address': address, 'phone': phone})
def readfile (fullPath):
    with open(fullPath, 'r') as openfile:
        csv_file = csv.DictReader(openfile)
        for row in csv_file:
            csvName = dict(row)["name"]
            csvAddress = dict(row)["address"]
            csvPhone = dict(row)["phone"]
            print (f"{csvName} {csvAddress} {csvPhone}")
if checkFolder:
    writetofile (fullPath, name, address, phone)
    readfile (fullPath)
else:
    print("folder doesn't exist")