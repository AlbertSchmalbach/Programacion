import os
import shutil

# Ruta donde estan los archivos a organizar
ruta = "C:/Users/KHAdmin/Documents/Confidencial/Albert/Archivos/Script_Python/Automatiza_Python/archivos/"

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

            # Crear ruta de destino
            destino = os.path.join(ruta, extensiones[ext], archivo)

            # Mover el archivo a la carpeta correspondiente
            shutil.move(ruta_archivo, destino)
            print(f"Moviendo {archivo} a {ext}/")
        else:
            print(f"Archivo {archivo} no se mueve, no es un tipo de archivo que queremos organizar.")
# Fin del script