import os
import shutil
import getpass

from tkinter import Tk, filedialog
from datetime import datetime

# Capturar usuario
usuario = getpass.getuser()

# Ruta donde estan los archivos a organizar
ventana = Tk()
ventana.withdraw()

ruta = filedialog.askdirectory(title="Carpeta a organizar")

# Crear carpetas para cada tipo de archivo
extensiones = {
    "jpg":"Img",
    "png":"Img",
    "pdf":"PDF",
    "mp4":"Videos",
    "docx":"Word",
    "xlsx":"Excel",
    "txt":"TXT"
}

for carpeta in set(extensiones.values()):

    ruta_carpeta = os.path.join(ruta, carpeta)

    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)


for archivo in os.listdir(ruta):
    
    ruta_archivo = os.path.join(ruta, archivo)

    if os.path.isfile(ruta_archivo):
        
        # Obtener la extension del archivo
        _, extension = os.path.splitext(archivo)
        ext = extension[1:].lower()  # quitar el punto de la extension

        if ext in extensiones:

            # Obtener fecha de modificacion
            fecha_mod = datetime.fromtimestamp(os.path.getmtime(ruta_archivo))
            sub_fecha = fecha_mod.strftime("%Y-%m") # Formatea a 2025-05 

            # Crear subcarpeta si no existe
            carpeta_tipo = os.path.join(ruta, extensiones[ext])
            carpeta_fecha = os.path.join(carpeta_tipo, sub_fecha)

            if not os.path.exists(carpeta_fecha):
                os.makedirs(carpeta_fecha)

            # Crear ruta de destino
            destino = os.path.join(carpeta_fecha, archivo)

            # Mover el archivo a la carpeta correspondiente
            shutil.move(ruta_archivo, destino)
            print(f"Moviendo {archivo} a {ext}/")

            with open(os.path.join(ruta, "log_organizacion.txt"), "a", encoding="utf-8") as log:
                log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Usuario: {usuario} - Movido: {archivo} -> {destino}\n")
        else:
            print(f"Archivo {archivo} no se mueve, no es un tipo de archivo que queremos organizar.")
# Fin del script