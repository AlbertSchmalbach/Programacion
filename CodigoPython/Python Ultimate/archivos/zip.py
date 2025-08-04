from zipfile import ZipFile
from pathlib import Path

with ZipFile("archivos/comprimidos.zip", "w") as zip:
    for path in Path().rglob("*.*"):
        print(path)
        if str(path) != "archivos/comprimidos.zip":
            zip.write(path)

# Leer
# with ZipFile("archivos/comprimidos.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("archivos/comprimidos.py")
#     print(
#         info.file_size,
#         info.compress_size
#     )

#     zip.extractall("archivos/descomprimidos")