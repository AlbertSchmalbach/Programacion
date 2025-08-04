from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/KHAdmin/Documents/CarpetaProtegida/Albert/Archivos/Script_Python/Python_16_Dias/archivos/Prueba.txt")

# print(carpeta.read_text())
# print(carpeta.name)
# print(carpeta.suffix)
# print(carpeta.stem)
# # print(carpeta.samefile())
# print(carpeta.read_bytes())

# if not  carpeta.exists():
#     print("Este archivo no existe")
# else:
#     print("La archivo existe")

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)