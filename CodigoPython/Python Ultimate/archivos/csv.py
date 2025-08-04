import csv
import os

# Escribir
# with open("archivos/archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([100, 1, "Este es un twit"])
#     writer.writerow([101, 2, "Este es otro twit"])

# Leer

# with open("archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     for r in reader:
#         print(r)

# Actualizar csv

with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "100":
            writer.writerow([100, 1, "tuit modificado"])
        else:
            writer.writerow(linea)
    os.remove("archivos/archivo.csv")
    os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")
