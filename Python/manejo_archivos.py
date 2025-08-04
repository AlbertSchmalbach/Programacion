import os

# 1.Lectura de un archivo:

# Abrir un archivo en modo lectura
archivo = open("datos.txt", "r")
# Leer el contenido del archivo
contenido = archivo.read()
# Cerrar el archivo
archivo.close()

# 2.Escritura en un archivo:

# Abrir un archivo en modo escritura
archivo = open("datos.txt", "w")
# Escribir en el archivo
archivo.write("Hola, mundo!")
# Cerrar el archivo
archivo.close()

# Obtener la ruta absoluta de un archivo
ruta_absoluta = os.path.abspath("datos.txt")
# Comprobar si un archivo existe
existe = os.path.exists("datos.txt")
# Obtener el nombre base de un archivo
nombre_base = os.path.basename("datos.txt")
# Unir dos rutas de archivo
ruta1 = "ruta1"
ruta2 = "ruta2"
ruta_completa = os.path.join(ruta1, ruta2)

# Leer el contenido del archivo
archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.close()
# Dividir el contenido en líneas
lineas = contenido.split("\n")
# Unir las líneas con un separador
nuevo_contenido = "\n".join(lineas)


