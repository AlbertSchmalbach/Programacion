import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
import shutil
import psutil
import platform
from speedtest import Speedtest
from datetime import datetime


# Función para escribir en el cuadro de texto
def escribir_resultado(text_widget, mensaje):
    text_widget.insert(tk.END, mensaje + "\n")
    text_widget.see(tk.END)


# Funciones del programa
def eliminar_archivos_temporales(text_widget):
    temp_path = os.environ.get('TEMP', None)
    if temp_path:
        try:
            shutil.rmtree(temp_path, ignore_errors=True)
            mensaje = "Archivos temporales eliminados correctamente."
        except Exception as e:
            mensaje = f"No se pudo eliminar los archivos temporales: {e}"
    else:
        mensaje = "No se encontró la carpeta de archivos temporales."
    escribir_resultado(text_widget, mensaje)


def vaciar_papelera_reciclaje(text_widget):
    try:
        recycle_bin = os.path.expanduser("~\\$Recycle.Bin")
        if os.path.exists(recycle_bin):
            shutil.rmtree(recycle_bin, ignore_errors=True)
            mensaje = "Papelera de reciclaje vaciada correctamente."
        else:
            mensaje = "No se encontró la papelera de reciclaje."
    except Exception as e:
        mensaje = f"Error al vaciar la papelera de reciclaje: {e}"
    escribir_resultado(text_widget, mensaje)


def reorganizar_archivos(text_widget):
    directory = tk.filedialog.askdirectory(title="Selecciona un directorio para organizar")
    if not directory:
        return
    try:
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                ext = os.path.splitext(file)[1][1:].upper()
                ext_folder = os.path.join(directory, ext)
                os.makedirs(ext_folder, exist_ok=True)
                shutil.move(file_path, ext_folder)
        mensaje = "Archivos reorganizados por extensión."
    except Exception as e:
        mensaje = f"No se pudo reorganizar los archivos: {e}"
    escribir_resultado(text_widget, mensaje)


def ver_informacion_sistema(text_widget):
    info = [
        f"Sistema Operativo: {platform.system()} {platform.release()} ({platform.version()})",
        f"Procesador: {platform.processor()}",
        f"Memoria RAM Total: {round(psutil.virtual_memory().total / (1024**3), 2)} GB",
        f"Uso de Memoria: {psutil.virtual_memory().percent}%",
        f"Uso de CPU: {psutil.cpu_percent(interval=1)}%",
    ]
    escribir_resultado(text_widget, "\n".join(info))


def realizar_test_velocidad(text_widget):
    try:
        st = Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        mensaje = f"Velocidad de descarga: {download_speed:.2f} Mbps | Velocidad de subida: {upload_speed:.2f} Mbps"
    except Exception as e:
        mensaje = f"No se pudo realizar el test de velocidad: {e}"
    escribir_resultado(text_widget, mensaje)


# Crear la interfaz gráfica
def crear_interfaz():
    root = tk.Tk()
    root.title("Optimizador de PC")

    # Crear el área de botones
    frame_botones = tk.Frame(root)
    frame_botones.pack(pady=10)

    # Crear el área de resultados
    text_resultados = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=70)
    text_resultados.pack(padx=10, pady=10)

    # Botones de acción
    botones = [
        ("Eliminar archivos temporales", lambda: eliminar_archivos_temporales(text_resultados)),
        ("Vaciar papelera de reciclaje", lambda: vaciar_papelera_reciclaje(text_resultados)),
        ("Reorganizar archivos", lambda: reorganizar_archivos(text_resultados)),
        ("Ver información del sistema", lambda: ver_informacion_sistema(text_resultados)),
        ("Test de velocidad de Internet", lambda: realizar_test_velocidad(text_resultados)),
    ]

    for texto, comando in botones:
        btn = tk.Button(frame_botones, text=texto, command=comando, width=30)
        btn.pack(pady=5)

    # Ejecutar la interfaz
    root.mainloop()


if __name__ == "__main__":
    crear_interfaz()
