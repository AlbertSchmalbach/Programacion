from pathlib import Path

path = Path("Rutas")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("codigo")

# print(path.iterdir())

# for p in path.iterdir():
#     print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos = [p for p in path.glob("*.py")]
archivos = [p for p in path.glob("**/*.py")]

print(archivos)