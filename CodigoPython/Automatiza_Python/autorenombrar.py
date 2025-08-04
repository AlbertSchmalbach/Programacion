import os
import getpass
from tkinter import Tk, filedialog

try:
    # Capturar usuario
    usuario = getpass.getuser()

    # Ruta donde estan los archivos a organizar
    ventana = Tk()
    ventana.withdraw()

    # carpeta="C:/Users/KHAdmin/Documents/Confidencial/Albert/Archivos/Script_Python/Automatiza_Python/imagenes"
    carpeta = filedialog.askdirectory(title="Elegir carpeta")

    prefijo = input('Dale un nombre a tus imagenes: ')

    if not prefijo:
        prefijo="imagen_"
        
    extensiones = (".jpg", ".png", ".jpeg")

    archivos = []

    for img in os.listdir(carpeta):

        ext = os.path.splitext(img)[1]

        if ext == ".PNG":
            ext = ext.lower()
            new_img = f"{os.path.splitext(img)[0]}{ext}"
            archivos.append(new_img)

        if img.endswith(extensiones):
            archivos.append(img)

    # Creacion del archivo para deshacer renombrado
    ruta_deshacer = os.path.join(carpeta, "deshacer.bat")

    with open(ruta_deshacer, "w", encoding="utf-8") as deshacer_mem:

        for n, nombre_actual in enumerate(archivos, start=1):
            extension_actual = os.path.splitext(nombre_actual)[1]
            nuevo_nombre = f"{prefijo}{n:03}{extension_actual}"
            ruta_actual = os.path.join(carpeta, nombre_actual)
            ruta_nueva = os.path.join(carpeta, nuevo_nombre)
            os.rename(ruta_actual, ruta_nueva)
            deshacer_mem.write(f'rename "{nuevo_nombre}" "{nombre_actual}"\n')
        
        deshacer_mem.write("del \"%~f0\"\n")

    print("Renombrado completo. Ejecuta el .bat generado para revertir cambios.")

except Exception as e:
    print(f'Error: {e}')