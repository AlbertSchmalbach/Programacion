import csv

productos = [
    ('Manzana', 1100),
    ('Uvas', 3500),
    ('Piña', 1500),
    ('Mango', 800),
    ('Sandia', 12000)
]

with open('frutas.csv', 'w', newline='\n') as filecsv:
    writer = csv.writer(filecsv, delimiter=',')
    for producto in productos:
        writer.writerow(producto)