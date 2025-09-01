# Escribir en un Archivo Existente
archivo = open('mi_archivo.txt', 'w')
archivo.write('Hola mundo')
archivo.close()

# Crear un Nuevo Archivo
nuevo_archivo = open('nuevo_archivo.txt', 'w')
nuevo_archivo.write('Este es un nuevo archivo creado en Python.')
nuevo_archivo.close()

# Escribir Varias Líneas en un Archivo Existente
archivo = open('mi_archivo.txt', 'w')
archivo.write('Linea 1\n')
archivo.write('Linea 2\n')
archivo.write('Linea 3\n')
archivo.close()

# Crear y Escribir en un Archivo CSV
import csv

# Ejemplo: Crear y escribir en un archivo CSV
datos = [("Nombre", "Edad"), ("Alberto", 42), ("Luz Saray", 23), ("Carol", 28)]

# Abrir (o crear) el archivo 'datos.csv' en modo escritura ('w'), usando newline="" para evitar líneas en blanco extra en Windows
with open('datos.csv', 'w', newline="") as archivo_csv:
    # Crear un objeto escritor CSV asociado al archivo abierto
    escritor_csv = csv.writer(archivo_csv)
    # Recorrer cada fila de la lista de datos
    for fila in datos:
        # Escribir la fila actual en el archivo CSV
        escritor_csv.writerow(fila)

# Escribir Datos Binarios en un Archivo

# Ejemplo: Escribir datos binarios en un archivo
datos_binarios = b"Estos son datos binarios."

with open("binario.dat", "wb") as archivo_binario:
    archivo_binario.write(datos_binarios)

# Crear un Nuevo Archivo JSON y Escribir en él
import json

# Ejemplo: Crear y escribir en un archivo JSON
datos_json = {"nombre": "Misuris Paola", "edad": 18, "ciudad": "Magangue"}

with open('datos.json', 'w') as archivo_json:
    json.dump(datos_json, archivo_json)