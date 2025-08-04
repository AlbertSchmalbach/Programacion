import json
from pathlib import Path

# escribir json
productos = [
    {"id": 1, "name": "Patines"},
    {"id": 2, "name": "Casco"},
    {"id": 3, "name": "Rodilleras"}
]

# data = json.dumps(productos)
# Path("archivos\productos.json").write_text(data)

# Leer json
data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
print(productos)