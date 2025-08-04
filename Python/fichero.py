import os
from urllib.request import urlopen

# Creación y escritura de ficheros
# f = open('saludo.txt', 'w', encoding='utf-8')
# f.write('¡Bienvenido a Python!')

# # Añadir datos a un fichero
# f = open('saludo.txt', 'a', encoding='utf-8')
# f.write('\n¡Hasta pronto!')

# Leer datos de un fichero
# f = open('saludo.txt', 'r')
# print(f.read())
# lineas = f.readlines()
# print(lineas)

# Cerrar un fichero
# f.close()

# La estructura with open(...) as

# with open('saludo.txt', 'w') as f:
#     f.write("Hola de nuevo")

# with open('saludo.txt', 'r') as f:
#     print(f.read())

# Renombrado y borrado de un fichero

# f = 'saludo.txt'
# if os.path.isfile(f):
#     os.rename(f, 'bienvenida.txt') # renombrado
#     print('¡Renombrado con exito!')
# else:
#     print('¡El fichero', f, 'no existe!')


# f = 'saludo.txt'
# if os.path.isfile(f):
#     os.remove(f)
#     print('¡Borrado con exito!')
# else:
#     print('¡El fichero', f, 'no existe!')

# Creación, cambio y eliminación de directorios

ruta = r'C:\Users\KHAdmin\Documents\CarpetaProtegida\Albert\Archivos\Script_Python'

# Devuelve una lista con los ficheros y directiorios contenidos en la ruta ruta:
# print(os.listdir(ruta)) 

# Crea un nuevo directorio en la ruta ruta:
carpeta = '\mi_carpeta'
# os.mkdir(ruta + carpeta)

# Devuelve una cadena con la ruta del directorio actual:
# print(os.getcwd())

# Cambia el directorio actual al indicado por la ruta ruta:
nueva_ruta = r'C:\Users\KHAdmin\Documents\CarpetaProtegida\Albert\Archivos'
# os.chdir(nueva_ruta)
# print(os.getcwd())

# Borra el directorio de la ruta ruta, siempre y cuando esté vacío.
# os.rmdir(ruta + carpeta)

# Leer un fichero de internet
f = urlopen('https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md')

datos = f.read()
print(datos.decode('utf-8'))