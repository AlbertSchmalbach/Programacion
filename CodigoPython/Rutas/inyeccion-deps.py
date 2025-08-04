from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

import db
import api
import graphql

dependencias = {
    "db":db,
    "api":api,
    "graphql":graphql
}

def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene funcion init o hay un fallo en la ruta")

list(map(load, paths))