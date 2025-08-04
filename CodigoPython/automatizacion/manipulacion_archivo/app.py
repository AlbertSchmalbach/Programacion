import os
from pathlib import Path, PurePath

ruta_os = os.getcwd()
ruta_path = Path.cwd()

# 1. Obtener ruta
print(f"Ruta con os: {ruta_os}")
print(f"Ruta con Path: {ruta_path}")

# 2. Listar archivos
# print(os.listdir('contacto'))
# print(list(Path('contacto').iterdir()))

# 3. Unir rutas
carpeta_actual = ruta_os


file_automatizacion = PurePath.joinpath(ruta_path, 'automatizacion')


# 4. Crear directorios
# os.mkdir('Prueba')
# Path('Prueba2').mkdir(exist_ok=True)

# os.makedirs(os.path.join('automatizacion', 'Script'))
# PurePath.joinpath(otra_actual, 'Code').mkdir(parents=True)

# 5. Renombrar archivos
# os.rename('contacto', 'contact')

# path_actual = Path('asistencia')
# path_obj = Path('Asistent')

# Path.rename(path_actual, path_obj)

os.chdir(file_automatizacion)

print(os.getcwd())

# 6. Comprobar si un archivo existe
# print(os.path.exists('Alberto_Schmalbach.txt'))

# archivo = Path('2025_Alberto_Schmalbach.txt')
# print(Path.exists(archivo))


for file in os.listdir():
    if file.endswith('.txt'):
        if not os.path.exists(file):
            os.rename(file, f'2025_{file}')
       
        else:
            print('El archivo ya existe en la carpeta')
            
# os.chdir(carpeta_actual)

print(Path.cwd())

# 7. metadata
# ruta_absoluta = os.path.abspath('automatizacion')
# print(ruta_absoluta)

script = Path('app.py')

print(script.resolve())
print(script.cwd())
print(script.name)
print(script.stem)
print(script.suffix)
print(script.stat().st_size)
