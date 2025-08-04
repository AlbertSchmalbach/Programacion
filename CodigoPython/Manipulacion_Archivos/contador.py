# contador.py
import sys
import os

# Nombre del archivo que almacenará el contador
archivo_contador = "contador.txt"

# Inicializar el contador
contador = 0

# Comprobar si el archivo existe y leer su valor
if os.path.exists(archivo_contador):
    try:
        with open(archivo_contador, "r") as archivo:
            contenido = archivo.read().strip()
            # Si el archivo no está vacío, intentamos convertir el contenido a un número
            if contenido:
                contador = int(contenido)
    except (ValueError, IOError):
        print("Error: Fichero corrupto.")
        sys.exit(1)
else:
    # Si el archivo no existe, crearlo con el valor 0
    with open(archivo_contador, "w") as archivo:
        archivo.write("0")

# Comprobar el argumento pasado al script
if len(sys.argv) > 1:
    argumento = sys.argv[1].lower()
    if argumento == "inc":
        contador += 1
    elif argumento == "dec":
        contador -= 1
    else:
        print(f"Valor actual del contador: {contador}")
        sys.exit(0)
else:
    print(f"Valor actual del contador: {contador}")
    sys.exit(0)

# Mostrar el valor actualizado del contador
print(f"Valor actual del contador: {contador}")

# Guardar el nuevo valor del contador en el archivo
try:
    with open(archivo_contador, "w") as archivo:
        archivo.write(str(contador))
except IOError:
    print("Error: No se pudo escribir en el fichero.")
    sys.exit(1)
