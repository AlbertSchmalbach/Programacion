# Abrir un Archivo para Lectura
try:
    archivo = open('mi_archivo.txt', 'r')
    contenido = archivo.read()
    archivo.close()
    print(contenido)
except FileNotFoundError:
    print("El archivo no se pudo encontrar.")
except Exception as e:
    print("Ocurrió un error:", e)

# Abrir un Archivo para Escritura
archivo = open('mi_archivo.txt', 'w')
archivo.write("¡Hola, esto es un nuevo archivo!\n")
archivo.close()

# Abrir un Archivo para Agregar Contenido
archivo = open("mi_archivo.txt", "a")
archivo.write("Añadiendo más contenido al archivo.\n")
archivo.close()

