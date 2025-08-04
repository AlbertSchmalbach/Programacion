def busqueda_lineal(lista, valor):
    for elemento in lista:
        if elemento == valor:
            return True
    return False

# Ejemplo de uso
mi_lista = [4, 2, 6, 1, 8, 3]
resultado = busqueda_lineal(mi_lista, 6)


def busqueda_binaria(lista, valor):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == valor:
            return True
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return False

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 6, 8]
resultado = busqueda_binaria(mi_lista, 6)
# print(resultado)

def ordenacion_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
# Ejemplo de uso
mi_lista = [4, 2, 6, 1, 8, 3]
resultado = ordenacion_burbuja(mi_lista)
# print(resultado)

def ordenacion_insercion(lista):
    n = len(lista)
    for i in range(1, n):
        valor_actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]
            j -= 1
            lista[j + 1] = valor_actual
    return lista
# Ejemplo de uso
mi_lista = [4, 2, 6, 1, 8, 3]
resultado = ordenacion_insercion(mi_lista)
print(resultado)