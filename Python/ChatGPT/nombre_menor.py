def estudiante_nombre_menor_ascii(estudiantes):
    estudiante_menor = min(estudiantes, key=lambda x: ord(x["nombre"][0]))
    return estudiante_menor

# Ejemplo de uso
lista_estudiantes = [
{'nombre': 'pablo', 'matematicas': 3.4, 'español': 5.0, 'ciencias': 2.9, 'literatura': 4.2, 'arte': 3.2},
{'nombre': 'andres', 'matematicas': 2.1, 'español': 5.0, 'ciencias': 3.0, 'literatura': 4.1, 'arte': 3.5},
{'nombre': 'daniela', 'matematicas': 5.0, 'español': 4.2, 'ciencias': 4.4, 'literatura': 3.5, 'arte': 4.7},
{'nombre': 'maria', 'matematicas': 3.2, 'español': 3.7, 'ciencias': 3.1, 'literatura': 4.7, 'arte': 3.4},
{'nombre': 'Pedro', 'matematicas': 5.0, 'español': 4.2, 'ciencias': 4.4, 'literatura': 3.5, 'arte': 4.7}
]

resultado = estudiante_nombre_menor_ascii(lista_estudiantes)
print("El estudiante con el nombre alfabéticamente menor (según ASCII) es:", resultado)
