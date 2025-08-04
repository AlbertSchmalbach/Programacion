def promedio_notas(*args):
    """
    La funcion recibe n argumentos:
    args: float()

    los suma y luego calcula el promedio
    Returns:
        el promedio de las notas

        Pruebas: python -m doctest nombre_archivo.py
        >>> promedio_notas(2.5, 4.2, 3.5)
        3.4

    """
    suma = sum(args)
    media = suma / len(args)
    return media

# print(promedio_notas(2.5, 4.2, 3.5))
