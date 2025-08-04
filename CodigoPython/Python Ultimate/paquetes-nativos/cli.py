import sys
import os
from pathlib import Path

def cli(args):
    if len(args)== 1:
        print("No se pasaron argumentos")
        return
    if len(args)!= 3:
        print("se necesitan 2 argumentos")
        return
    
    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe")
        return
    
    destino = args[2]
    d = Path(origen)
    if d.exists():
        print("El destino no puede existir")
        return
    
    os.rename(str(origen), str(destino))
    print("Archivo renombrado con existo")

cli(sys.argv)