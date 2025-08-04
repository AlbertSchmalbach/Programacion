from io import open

# escritura

# texto = "Hola mundo"

# archivo = open("archivos/hola-mundo.txt", "w", encoding="utf-8")
# archivo.write(texto)
# archivo.close()

# lectura

# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)


# lectura como lista

# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# with open("archivos/archivo.txt", "r", encoding="utf-8") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# agregar texto sin borrar anterior

# with open("archivos/hola-mundo.txt", "a+", encoding="utf-8") as archivo:
#     archivo.write("\n Chao lola, 😥")

# lectura y escritura

with open("archivos/hola-mundo.txt", "r+", encoding="utf-8") as archivo:
    texto = archivo.readlines()
    archivo.seek(0) #leer primera linea de texto
    texto[0] = "Luz Saray Atencia 😍"
    archivo.writelines(texto)
