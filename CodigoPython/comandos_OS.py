import os, platform, cleaner

cleaner.cleaning()

# module platform windows
sistema = platform.uname()
print(f'Sistema Operativo: {sistema.system}')
print(f'Version: {sistema.release}')
print(f'Procesador: {sistema.machine}')

# module os
# os.uname() en unix
# print(os.name)
# Crear directorio => mkdir()
# os.mkdir("./my_first_directory2")

# listar contenido de directorio actual => listdir()
# print(os.listdir())

# Crear directorio dentro de otro => makedirs() - cambiar de directorio => chdir()
# os.makedirs("my_first_directory3/my_second_directory")
# os.chdir("my_first_directory3")
# print(os.listdir())

# ruta actual => getcwd()
# os.chdir("my_first_directory3")
# print(os.getcwd())
# os.chdir("my_second_directory")
print(os.getcwd())

# Remover directorios => rmdir()
# os.rmdir("./my_first_directory2")
# print(os.listdir())

# Remover directorios y subdirectorios => removedirs()
# os.removedirs("my_first_directory3/my_second_directory")