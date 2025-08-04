# LEER FICHERO

# fichero = open("datos.txt", "r", encoding="utf-8")

# Método read()
# print(fichero.read())

# Método readline()
# print(fichero.readline())
# print(fichero.readline())

# caracter = fichero.readline(1)
# while caracter != "":
#     print(caracter)
#     caracter = fichero.readline(1)

# lineas = fichero.readlines()
# print(lineas)

# lineas = fichero.readlines()
# for linea in lineas:
#     print(linea)

# ‘r’: Por defecto, para leer el fichero.
# ‘w’: Para escribir en el fichero.
# ‘x’: Para la creación, fallando si ya existe.
# ‘a’: Para añadir contenido a un fichero existente.
# ‘b’: Para abrir en modo binario.

# Cerrar fichero
# fichero.close()

# try:
#     # Usar el fichero
#     pass
# finally:
#     # Esta sección es siempre ejecutada
#     fichero.close()

# with()
# with open('datos.txt', 'r', encoding='utf-8') as fichero:
#     linea = fichero.readline()
#     while linea != '':
#         print(linea, end='')
#         linea = fichero.readline()

# with open('datos.txt', 'r', encoding='utf-8') as fichero:
#     for linea in fichero.readlines():
#         print(linea, end='')

# with open('datos.txt', 'r' encoding='utf-8') as fichero:
#     for linea in fichero:
#         print(linea, end=''),

# CREAR FICHERO

# Abrimos el fichero
# fichero = open('fichero_guardado.txt', 'w', encoding='utf-8') # Crea y reemplaza
# fichero = open('fichero_guardado.txt', 'a') # Añade al existente

# Tenemos unos datos que queremos guardar
lista = ["Manzana\n", "Pera\n", "Plátano\n", "Banano\n", "Sandia\n"]

# Guardamos la lista en el fichero
# 1. forma
# for fruta in lista:
#     fichero.write(fruta + "\n")

# 2. forma
# fichero.writelines(lista)

# Cerramos el fichero
# fichero.close()

with open('fichero_guardado.txt', 'w', encoding='utf-8') as fichero:
    fichero.writelines(lista)


# EJEMPLO PRACTICO:

# Escribe un mensaje en un fichero
def escribe_fichero(mensaje):
    with open('fichero_comunicacion.txt', 'w') as fichero:
        fichero.write(mensaje)

# Leer el mensaje del fichero        
def lee_fichero():
    mensaje = ""
    with open('fichero_comunicacion.txt', 'r') as fichero:
        mensaje = fichero.read()
    # Borra el contenido del fichero para dejarlo vacío
    f = open('fichero_comunicacion.txt', 'w')
    f.close()
    return mensaje

escribe_fichero("Programando manipulacion de ficheros con Python")
print(lee_fichero())