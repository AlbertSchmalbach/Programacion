from io import open

# Creación y escritura

texto = "Una línea con texto\nOtra línea con texto"

# Ruta donde crearemos el fichero, w indica escritura (puntero al principio)
fichero = open('fichero.txt','w', encoding='utf')

# Escribimos el texto
fichero.write(texto)

# Cerramos el fichero
fichero.close()

# Lectura

# Ruta donde leeremos el fichero, r indica lectura (por defecto ya es r)
fichero = open('fichero.txt','r', encoding='utf-8')

# Lectura completa
# texto = fichero.read()
# Leempos creando una lista de líneas
texto = fichero.readlines()

# Cerramos el fichero
fichero.close()

print(texto)

with open("fichero.txt", "r", encoding="utf-8") as fichero:
    for linea in fichero:
        print(linea)

# Extensión

# Ruta donde leeremos el fichero, a indica extensión (puntero al final)
fichero = open('fichero.txt','a', encoding='utf-8')
# La variante 'a+' permite crear el fichero si no existe:
# fichero = open('fichero_inventado.txt','a+')

fichero.write('\nOtra línea más abajo del todo')

fichero.close()

# Manejando el puntero

fichero = open('fichero.txt','r', encoding='utf-8')
fichero.seek(0)   # Puntero al principio
fichero.read(10)  # Leemos 10 carácteres

# Leemos la primera línea y situamos el puntero al principio de la segunda
fichero.seek( len(fichero.readline()) )

# Leemos todo lo que queda del puntero hasta el final
fichero.read()

# Lectura con escritura

# Creamos un fichero de prueba con 4 líneas
fichero = open('fichero2.txt','w', encoding='utf-8')
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4"
fichero.write(texto)
fichero.close()

# Lo abrimos en lectura con escritura y escribimos algo
fichero = open('fichero2.txt','r+', encoding='utf-8')
fichero.write("0123456")

# Volvemos a poner el puntero al inicio y leemos hasta el final
fichero.seek(0)
fichero.read()
fichero.close()

# Modificar una línea

fichero = open('fichero2.txt','r+', encoding="utf-8")
texto = fichero.readlines()

# Modificamos la línea que queramos a partir del índice
texto[2] = "Esta es la línea 3 modificada\n"

# Volvemos a ponter el puntero al inicio y reescribimos
fichero.seek(0)
fichero.writelines(texto)
fichero.close()

# Leemos el fichero de nuevo
with open("fichero2.txt", "r", encoding="utf-8") as fichero:
    print(fichero.read())