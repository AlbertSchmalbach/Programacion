"""Module providingFunction printing python version."""
import sys


def conteo_de_materias(nombre_materia_1: str, nombre_materia_2: str, nombre_materia_3: str) -> int:
    """Function printing python version."""
    print(sys.version)

    area1 = nombre_materia_1.lower()
    area2 = nombre_materia_2.lower()
    area3 = nombre_materia_3.lower()

    contador = 0

    if area1.find('programacion') != -1 or area1.find('matematica') != -1 or area1('filosofia') != -1 or area1.find('literatura') != -1:
        contador += 1
    if area2.find('programacion') != -1 or area2.find('matematica') != -1 or area2.find('filosofia') != -1 or area2.find('literatura') != -1:
        contador += 1
    if area3.find('programacion') != -1 or area3.find('matematica') != -1 or area3.find('filosofia') != -1 or area3.find('literatura') != -1:
        contador += 1
    return contador


print(conteo_de_materias('introduccion a la programacion',
      'cimientos estructurales', 'algoritmica y programacion orientada por objetos I'))
