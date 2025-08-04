import os
from pathlib import Path

# ruta = os.getcwd()
# ruta = os.chdir(r"C:\Users\KHAdmin\Documents\CarpetaProtegida\Albert\Archivos\Script_Python\Python_16_Dias\Proyectos") #Abrir archivo de otra ubicacion

# ruta = os.makedirs(r"C:\Users\KHAdmin\Documents\CarpetaProtegida\Albert\Archivos\Script_Python\Python_16_Dias\Carpeta_Dir") #Crear carpeta

# archivo = open("otro_archivo.txt")

# ruta = r"C:\Users\KHAdmin\Documents\CarpetaProtegida\Albert\Archivos\Script_Python\Python_16_Dias\archivos\Prueba.txt"

# elemento = os.path.basename(ruta)
# elemento = os.path.dirname(ruta)
# elemento = os.path.split(ruta)

# ruta = os.rmdir(r"C:\Users\KHAdmin\Documents\CarpetaProtegida\Albert\Archivos\Script_Python\Python_16_Dias\Carpeta_dir") 

carpeta = Path("/Users/KHAdmin/Documents/CarpetaProtegida/Albert/Archivos/Script_Python/Python_16_Dias/Prueba")

archivo = carpeta / "texto.txt"

mi_archivo = open(archivo)
print(mi_archivo.read())