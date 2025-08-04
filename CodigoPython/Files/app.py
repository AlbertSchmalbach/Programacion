# Lectura de archivos
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

# Escritura de archivos
archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
