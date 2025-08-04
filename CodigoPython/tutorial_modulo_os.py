import os

# 1. Obtener el Directorio Actual
current_directory = os.getcwd()
print(f"Directorio actual: {current_directory}")

# 2. Cambiar el Directorio Actual
os.chdir(current_directory+'/contacto')
print(f"Nuevo directorio actual: {os.getcwd()}")

# 3. Listar Archivos en un Directorio
files_and_directories = os.listdir(current_directory+'/contacto')
print(f"Contenido del directorio: {files_and_directories}")

# 4. Crear un Nuevo Directorio
# os.mkdir(current_directory+'/contacto/mis_datos')
# os.makedirs('/ruta/a/nuevo/directorio/con/padres')


# 5. Eliminar un Directorio
# os.rmdir(current_directory+'/contacto/mis_datos')
# os.removedirs('/ruta/del/directorio/con/padres')

# 6. Eliminar un Archivo
# os.remove(current_directory+'/contacto/texto_2.txt')

# 7. Renombrar o Mover Archivos y Directorios
# os.rename('/ruta/actual/del/archivo_o_directorio', '/nueva/ruta/o/nombre')

# 8. Información del Sistema
system_name = os.name
print(f"Nombre del sistema operativo: {system_name}")

# Para obtener más detalles del sistema:
# info = os.uname()
# print(f"Información del sistema: {info}")

# 9. Variables de Entorno
path = os.getenv('PATH')
# print(f"PATH: {path}")

# Ejemplo Práctico

import os

# Paso 1: Crear la estructura de directorios
proyecto_dir = 'mi_proyecto'
data_dir = os.path.join(proyecto_dir, 'data')
scripts_dir = os.path.join(proyecto_dir, 'scripts')

# Crear directorios
os.makedirs(data_dir)
os.makedirs(scripts_dir)

# Crear archivos dentro de 'data'
with open(os.path.join(data_dir, 'input.txt'), 'w') as f:
    f.write('Este es el archivo de entrada.')

with open(os.path.join(data_dir, 'output.txt'), 'w') as f:
    f.write('Este es el archivo de salida.')

# Crear archivo dentro de 'scripts'
with open(os.path.join(scripts_dir, 'process.py'), 'w') as f:
    f.write('# Este es el script de procesamiento.\nprint("Procesando datos...")')

print("Estructura de directorios y archivos creada.")

# Paso 2: Listar el contenido
print("\nContenido de 'mi_proyecto':", os.listdir(proyecto_dir))
print("Contenido de 'data':", os.listdir(data_dir))
print("Contenido de 'scripts':", os.listdir(scripts_dir))

# Paso 3: Eliminar archivos y directorios

# Eliminar archivos en 'data'
os.remove(os.path.join(data_dir, 'input.txt'))
os.remove(os.path.join(data_dir, 'output.txt'))

# Eliminar archivo en 'scripts'
os.remove(os.path.join(scripts_dir, 'process.py'))

# Eliminar directorios
os.rmdir(data_dir)
os.rmdir(scripts_dir)
os.rmdir(proyecto_dir)

print("\nEstructura de directorios y archivos eliminada.")








