import csv

with open('frutas.csv', newline='\n') as filecsv:
    reader = csv.reader(filecsv, delimiter=',')
    for nombre, precio in reader:
        print(nombre, precio)