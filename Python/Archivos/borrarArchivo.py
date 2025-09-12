import os
import shutil
from pathlib import Path

# 1. Eliminar archivo en Python

archivo_eliminar = input("Nombre del archivo a eliminar: ")

ruta = Path.cwd() / archivo_eliminar

if os.path.exists(ruta):
    os.remove(ruta)
    print("Archivo eliminado")
else:
    print("Archivo no exitse")

# 2. Eliminar carpeta en Python

# Ruta de la carpeta que deseas eliminar
# carpeta_a_eliminar = "archivo_ejemplo"

# Eliminar la carpeta completa con su contenido
# shutil.rmtree(carpeta_a_eliminar)