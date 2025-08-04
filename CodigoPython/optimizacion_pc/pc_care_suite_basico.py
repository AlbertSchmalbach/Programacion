import os
import shutil
import psutil
import platform
import subprocess
from speedtest import Speedtest
from datetime import datetime
from pathlib import Path
import ctypes
import sys


# Función para escribir en el reporte
def escribir_reporte(tarea, resultado):
    with open("reporte_tareas.txt", "a") as reporte:
        reporte.write(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] - {tarea}: {resultado}\n")


def is_admin():
    """Verifica si el script se está ejecutando con privilegios de administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def eliminar_archivos_temporales():
    temp_path = os.environ.get('TEMP', None)
    if temp_path:
        try:
            shutil.rmtree(temp_path, ignore_errors=True)
            mensaje = "Archivos temporales eliminados correctamente."
            print(f"[INFO] {mensaje}")
            escribir_reporte("Eliminar archivos temporales", mensaje)
        except Exception as e:
            mensaje = f"No se pudo eliminar los archivos temporales: {e}"
            print(f"[ERROR] {mensaje}")
            escribir_reporte("Eliminar archivos temporales", mensaje)
    else:
        mensaje = "No se encontró la carpeta de archivos temporales."
        print(f"[ERROR] {mensaje}")
        escribir_reporte("Eliminar archivos temporales", mensaje)


def vaciar_papelera_reciclaje():
    """Vacia la papelera de reciclaje (Windows)."""
    try:
        recycle_bin = Path("C:\\$Recycle.Bin")
        if recycle_bin.exists():
            shutil.rmtree(recycle_bin, ignore_errors=True)
            print("Papelera de reciclaje vaciada correctamente.")
        else:
            print("No se encontró la papelera de reciclaje.")
    except Exception as e:
        print(f"Error al vaciar la papelera de reciclaje: {e}")


def reorganizar_archivos():
    directory = input(
        "Introduce el directorio que deseas organizar (ejemplo: C:\\Users\\Usuario\\Desktop): ")
    try:
        directory = Path(directory)
        if not directory.exists():
            mensaje = "El directorio no existe."
            print(f"[ERROR] {mensaje}")
            escribir_reporte("Reorganizar archivos", mensaje)
            return

        for file in directory.iterdir():
            if file.is_file():
                ext = file.suffix[1:]  # Obtener la extensión sin el punto
                ext_folder = directory / ext.upper()
                ext_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(ext_folder))
        mensaje = "Archivos reorganizados por extensión."
        print(f"[INFO] {mensaje}")
        escribir_reporte("Reorganizar archivos", mensaje)
    except Exception as e:
        mensaje = f"No se pudo reorganizar los archivos: {e}"
        print(f"[ERROR] {mensaje}")
        escribir_reporte("Reorganizar archivos", mensaje)
    

def liberar_espacio_disco():
    """Calcula el espacio en disco y sugiere liberar espacio."""
    try:
        total, used, free = shutil.disk_usage("/")
        total_gb = total // (1024**3)
        used_gb = used // (1024**3)
        free_gb = free // (1024**3)

        mensaje = (f"Espacio total: {total_gb} GB | Usado: {used_gb} GB | Libre: {free_gb} GB")
        print(f"[INFO] {mensaje}")

        if free_gb < 10:
            print("El espacio libre en disco es bajo. Se recomienda liberar espacio.")
            eliminar_archivos_temporales()
            vaciar_papelera_reciclaje()

        escribir_reporte("Liberar espacio en disco", mensaje)
    except Exception as e:
        mensaje = f"No se pudo calcular el espacio en disco: {e}"
        print(f"[ERROR] {mensaje}")
        escribir_reporte("Liberar espacio en disco", mensaje)


def borrar_datos_navegacion():
    browser = input("Seleccione el navegador (Chrome/Edge): ").strip().lower()
    try:
        if browser == 'chrome':
            chrome_cache = os.path.expanduser('~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache')
            shutil.rmtree(chrome_cache, ignore_errors=True)
            mensaje = "Datos de navegación de Chrome eliminados."
            print(f"[INFO] {mensaje}")
        elif browser == 'edge':
            edge_cache = os.path.expanduser('~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache')
            shutil.rmtree(edge_cache, ignore_errors=True)
            mensaje = "Datos de navegación de Edge eliminados."
            print(f"[INFO] {mensaje}")
        else:
            mensaje = "Navegador no reconocido."
            print(f"[ERROR] {mensaje}")
        escribir_reporte("Borrar datos de navegación", mensaje)
    except Exception as e:
        mensaje = f"No se pudieron eliminar los datos de navegación: {e}"
        print(f"[ERROR] {mensaje}")
        escribir_reporte("Borrar datos de navegación", mensaje)

def ver_informacion_sistema():
    info = [
        f"Sistema Operativo: {platform.system()} {platform.release()} ({platform.version()})",
        f"Procesador: {platform.processor()}",
        f"Memoria RAM Total: {round(psutil.virtual_memory().total / (1024**3), 2)} GB",
        f"Uso de Memoria: {psutil.virtual_memory().percent}%",
        f"Uso de CPU: {psutil.cpu_percent(interval=1)}%",
        f"Espacio Total en Disco: {round(psutil.disk_usage('/').total / (1024**3), 2)} GB",
        f"Espacio Ocupado: {round(psutil.disk_usage('/').used / (1024**3), 2)} GB",
        f"Espacio Libre: {round(psutil.disk_usage('/').free / (1024**3), 2)} GB",
    ]
    print("=== Información del Sistema ===")
    for line in info:
        print(line)
    escribir_reporte("Ver información del sistema", " | ".join(info))

def realizar_test_velocidad():
    print("Realizando test de velocidad, por favor espere...")
    print()
    try:
        st = Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convertir a Mbps
        upload_speed = st.upload() / 1_000_000  # Convertir a Mbps
        mensaje = f'''
        - Velocidad de descarga: {download_speed:.2f} Mbps  
        - Velocidad de subida: {upload_speed:.2f}    Mbps'''
        print(f"[INFO] {mensaje}")
        print()
        escribir_reporte("Test de velocidad de Internet", mensaje)
    except Exception as e:
        mensaje = f"No se pudo realizar el test de velocidad: {e}"
        print(f"[ERROR] {mensaje}")
        escribir_reporte("Test de velocidad de Internet", mensaje)

def menu():
    while True:
        print("\n=== OPTIMIZADOR DE PC ===")
        print("1. Eliminar archivos temporales")
        print("2. Vaciar papelera de reciclaje")
        print("3. Reorganizar archivos")
        print("4. Liberar espacio en disco")
        print("5. Borrar datos de navegación")
        print("6. Realizar test de velocidad de Internet")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        print()
        print()

        if opcion == '1':
            eliminar_archivos_temporales()
        elif opcion == '2':
            vaciar_papelera_reciclaje()
        elif opcion == '3':
            reorganizar_archivos()
        elif opcion == '4':
            liberar_espacio_disco()
        elif opcion == '5':
            borrar_datos_navegacion()
        elif opcion == '6':
            realizar_test_velocidad()
        elif opcion == '7':
            print("Saliendo del programa. ¡Adiós!")
            break   
        else:
            print("[ERROR] Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    if not is_admin():
        print("El programa necesita permisos de administrador para ejecutarse.")
        print("Reiniciando con permisos elevados...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1
        )
        sys.exit()
    menu()
