matriz = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

# Recorrer matriz - 1 forma
# for fila in matriz:
#     for element in fila:
#         print(element, end=' ')
#     print()

 # Recorrer matriz - 2 forma
for index_fila in range(0, len(matriz)):
    for index_columnas in range(0, len(matriz[index_fila])):
      print(matriz[index_fila][index_columnas], end=' ')
    print()