import os
import shutil
import tempfile
from pathlib import Path
import ctypes
import sys

def is_admin():
    """Verifica si el script se está ejecutando con privilegios de administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def clear_temp_files():
    """Elimina los archivos temporales."""
    temp_dir = tempfile.gettempdir()
    try:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"No se pudo eliminar: {file_path}, Error: {e}")
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(dir_path, ignore_errors=True)
                except Exception as e:
                    print(f"No se pudo eliminar: {dir_path}, Error: {e}")
        print("Archivos temporales eliminados correctamente.")
    except Exception as e:
        print(f"Error al eliminar archivos temporales: {e}")

def clear_recycle_bin():
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

def reorganize_files(directory):
    """
    Reorganiza archivos en el directorio dado, clasificándolos por extensión.
    Crea carpetas para cada tipo de archivo.
    """
    try:
        directory = Path(directory)
        if not directory.exists():
            print("El directorio especificado no existe.")
            return

        for file in directory.iterdir():
            if file.is_file():
                ext = file.suffix[1:]  # Obtener la extensión sin el punto
                ext_folder = directory / ext.upper()
                ext_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(ext_folder))
        print("Archivos reorganizados correctamente.")
    except Exception as e:
        print(f"Error al reorganizar archivos: {e}")

def menu():
    """Muestra un menú al usuario para elegir tareas."""
    while True:
        print("\n=== OPTIMIZADOR DE PC ===")
        print("1. Eliminar archivos temporales")
        print("2. Vaciar papelera de reciclaje")
        print("3. Reorganizar archivos en un directorio")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            clear_temp_files()
        elif opcion == "2":
            clear_recycle_bin()
        elif opcion == "3":
            directory = input("Introduce el directorio que deseas organizar (ejemplo: C:\\Users\\Usuario\\Desktop): ")
            reorganize_files(directory)
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    if not is_admin():
        print("El programa necesita permisos de administrador para ejecutarse.")
        print("Reiniciando con permisos elevados...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1
        )
        sys.exit()
    else:
        menu()
