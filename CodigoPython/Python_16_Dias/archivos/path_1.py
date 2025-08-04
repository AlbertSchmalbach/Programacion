from pathlib import Path

# guia = Path("Carpeta", "archivo")
base = Path.home()
# print(base)
# guia = Path(base, "Documents", "CarpetaProtegida", "Albert", "Archivos", "Script_Python", "Python_16_Dias", "archivos")
# print(guia)

# for txt in Path(guia).glob("**/*.txt"):
#     print(txt)

ruta = Path("principal", "archivos", "folders", "ficheros")

# print(ruta)

ruta_relativa = ruta.relative_to(Path("archivos"))

print(ruta_relativa)


