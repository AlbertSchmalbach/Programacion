import getpass
import os
import platform
# Trabajar con archivos y directorios

ruta_actual = os.getcwd() # Obtiene el directorio actual.
print(ruta_actual)
listar_dir = os.listdir(ruta_actual) # Lista los archivos y carpetas en un directorio.
# print(listar_dir)
New_carpeta = os.path.join(ruta_actual, "Carpeta_New")
# os.mkdir(New_carpeta) # Crea un nuevo directorio.
# src = ruta_actual + "\Carpeta_New"
dst = os.path.join(ruta_actual, "New_Name")
# os.rename(New_carpeta, dst)

# Gestión de procesos

os.system("echo Hola Luz Saray")
# os.system("dir")

if platform.system() == "Windows":
    os.system("dir")
else:
    os.system("ls")

# Variables de entorno

# Obtener una variable de entorno
user = getpass.getuser()
usuario = os.getenv("USERNAME")
print(user)
print(f"El usuario actual es: {usuario}")
