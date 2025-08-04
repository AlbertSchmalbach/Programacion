import os
import shutil
import psutil
import platform
import subprocess
from datetime import datetime
from speedtest import Speedtest
from pathlib import Path
import ctypes
import sys
import wmi
from win32com.client import Dispatch
from tkinter import filedialog as FileDialog

# ========================================
# PC Care Suite
# Autor: Alberto Schmalbach Lopez
# Descripción:
# Herramienta multifuncional para optimización
# y mantenimiento de sistemas Windows.
# ========================================



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
    directory = FileDialog.askdirectory(title="Abrir Directorio")
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
    try:
        st = Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convertir a Mbps
        upload_speed = st.upload() / 1_000_000  # Convertir a Mbps
        mensaje = f"Velocidad de descarga: {download_speed:.2f} Mbps | Velocidad de subida: {upload_speed:.2f} Mbps"
        print(f"[INFO]")
        # Print the results
        print("Download Speed: {:.2f} Mbps".format(download_speed))
        print("Upload Speed: {:.2f} Mbps".format(upload_speed))
        escribir_reporte("Test de velocidad de Internet", mensaje)
    except Exception as e:
        mensaje = f"No se pudo realizar el test de velocidad: {e}"
        print(f"[ERROR] {mensaje}")
        escribir_reporte("Test de velocidad de Internet", mensaje)

# Nueva función: Crear un punto de restauración
def crear_punto_de_restauracion(name="PythonRestorePoint"):
    try:
        # Obtener el objeto SystemRestore
        obj = Dispatch("WbemScripting.SWbemLocator").ConnectServer(".", "root/default").Get("SystemRestore")

        # Crear el punto de restauración
        result = obj.CreateRestorePoint(name, 0, 100)

        if result == 0:
            mensaje = "Punto de restauración creado exitosamente."
            print(f"[INFO] {mensaje}")
        else:
            print("Failed")
        escribir_reporte("Crear punto de restauración", mensaje)
        
    except Exception as e:
        mensaje = f"No se pudo crear el punto de restauración: {e}"
        print(f"[ERROR] {mensaje}")
        escribir_reporte("Crear punto de restauración", mensaje)

# Nueva función: Desinstalar un programa
def desinstalar_programa():
    programa = input("Ingrese el nombre del programa que desea desinstalar: ")
    confirmacion = input(
        f"¿Está seguro que desea desinstalar {programa}? Esto no se puede deshacer (S/N): ").strip().lower()
    if confirmacion == 's':
        try:
            subprocess.run(f"wmic product where name=\"{programa}\" call uninstall",
                           shell=True, check=True)
            mensaje = f"El programa {programa} fue desinstalado correctamente."
            print(f"[INFO] {mensaje}")
            escribir_reporte("Desinstalar programa", mensaje)
        except Exception as e:
            mensaje = f"No se pudo desinstalar el programa {programa}: {e}"
            print(f"[ERROR] {mensaje}")
            escribir_reporte("Desinstalar programa", mensaje)
    else:
        print("Desinstalación cancelada.")

# Nueva función: Listar y formatear unidades de disco
def listar_y_formatear_unidades():
    print("=== Listado de unidades de disco ===")
    unidades = [disk.device for disk in psutil.disk_partitions()]
    sistema = os.environ.get("SystemDrive", "C:")  # Unidad del sistema (por defecto C:)
    
    for unidad in unidades:
        try:
            uso = shutil.disk_usage(unidad)
            print(f"Unidad: {unidad} | Total: {uso.total // (1024**3)} GB | Libre: {uso.free // (1024**3)} GB")
        except Exception:
            print(f"Unidad: {unidad} (Error al obtener información)")

    print("\n=== Formatear unidades USB ===")
    for disk in psutil.disk_partitions(all=False):
        if "removable" in disk.opts.lower():
            print(f"Unidad USB detectada: {disk.device}")

    unidad_formatear = input("\nIngrese la letra de la unidad USB que desea formatear (ejemplo: D:\\): ").strip().upper()
    
    if unidad_formatear == sistema:
        print("[ERROR] No puede formatear la unidad del sistema.")
        return
    
    if not any(unidad_formatear in disk.device for disk in psutil.disk_partitions(all=False) if "removable" in disk.opts.lower()):
        print("[ERROR] La unidad seleccionada no es una unidad USB o no existe.")
        return

    confirmacion = input(f"¿Está seguro que desea formatear la unidad {unidad_formatear}? (S/N): ").strip().lower()
    if confirmacion == 's':
        try:
            subprocess.run(["format", unidad_formatear, "/FS:NTFS", "/Q", "/Y"], check=True, shell=True)
            print(f"[INFO] Unidad {unidad_formatear} formateada correctamente.")
            escribir_reporte("Formatear unidad USB", f"Unidad {unidad_formatear} formateada.")
        except Exception as e:
            print(f"[ERROR] No se pudo formatear la unidad: {e}")
            escribir_reporte("Formatear unidad USB", f"Error al formatear unidad {unidad_formatear}: {e}")
    else:
        print("Operación cancelada.")
        
# Nueva función: Restaurar a valores de fábrica
def restaurar_valores_fabrica():
    print("Este proceso restaurará el sistema a sus valores de fábrica.")
    print("Se recomienda crear un punto de restauración antes de continuar.")
    crear_punto = input("¿Desea crear un punto de restauración ahora? (S/N): ").strip().lower()
    if crear_punto == 's':
        crear_punto_de_restauracion()
    confirmacion = input(
        "¿Está seguro que desea restaurar el sistema a los valores de fábrica? Esto no se puede deshacer (S/N): ").strip().lower()
    if confirmacion == 's':
        try:
            subprocess.run("systemreset -factoryreset", shell=True)
            mensaje = "El sistema fue restaurado a sus valores de fábrica."
            print(f"[INFO] {mensaje}")
            escribir_reporte("Restaurar valores de fábrica", mensaje)
        except Exception as e:
            mensaje = f"No se pudo restaurar el sistema: {e}"
            print(f"[ERROR] {mensaje}")
            escribir_reporte("Restaurar valores de fábrica", mensaje)
    else:
        print("Restauración cancelada.")

# Actualización del menú
def menu():
    while True:
        print("\n=== OPTIMIZADOR DE PC ===")
        print("1. Eliminar archivos temporales")
        print("2. Vaciar papelera de reciclaje")
        print("3. Reorganizar archivos")
        print("4. Liberar espacio en disco")
        print("5. Borrar datos de navegación")
        print("6. Ver información del sistema")
        print("7. Realizar test de velocidad de Internet")
        print("8. Crear un punto de restauración")
        print("9. Desinstalar un programa")
        print("10. Listar y formatear unidades de disco")
        print("11. Restaurar sistema a valores de fábrica")
        print("12. Salir")
        opcion = input("Seleccione una opción: ")
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
            ver_informacion_sistema()
        elif opcion == '7':
            realizar_test_velocidad()
        elif opcion == '8':
            crear_punto_de_restauracion()
        elif opcion == '9':
            desinstalar_programa()
        elif opcion == '10':
            listar_y_formatear_unidades()
        elif opcion == '11':
            restaurar_valores_fabrica()
        elif opcion == '12':
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
