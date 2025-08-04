# Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

# Borrar los elementos duplicados.
# Ordenar la lista de mayor a menor.
# Eliminar todos los números impares.
# Realizar una suma de todos los números que quedan.
# Añadir como primer elemento de la lista la suma realizada.
# Devolver la lista modificada.
# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:

# Creamos funcion
def modificar(lista):
    # Borrar los elementos duplicados.
    lista = set(lista)
    lista_sin_duplicados = list(lista)
    print(f'Lista sin duplicados: {lista_sin_duplicados}')
    # Ordenar la lista de mayor a menor.
    lista_sin_duplicados.sort(reverse=True)
    print(f'Lista de mayor a menor: {lista_sin_duplicados}')
    # Eliminar todos los números impares.
    lista_pares = []
    for n in lista_sin_duplicados:
        if n % 2 == 0:
            lista_pares.append(n)
    print(f'Lista sin impares: {lista_pares}')
    # Realizar una suma de todos los números que quedan.
    sum_lista = sum(lista_pares)
    print(f'Suma de los numeros restantes: {sum_lista}')
    # Añadir como primer elemento de la lista la suma realizada.
    lista_pares.insert(0, sum_lista)
    print(f'Lista con total en la primera posicion: {lista_pares}')
    # Devolver la lista modificada.
    lista = lista_pares
    # return lista
    print(f'Lista devuelta: {lista}')

    

lista = [4, 8, 15, 18, 18, 16, 4, 4, 14, 4, 12, 15, 10, 17, 11]

modificar(lista)

# nueva_lista = modificar(lista)
# print( nueva_lista[0] == sum(nueva_lista[1:]) )