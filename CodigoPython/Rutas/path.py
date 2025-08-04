from pathlib import Path

path = Path("Mi_Carpeta/archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.absolute()
)

p = path.with_name("prueba.py")
p = path.with_stem("codigo")
p = path.with_suffix(".bat")

print(p)