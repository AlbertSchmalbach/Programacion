def binary_search(arr, target):
    """
    Realiza una búsqueda binaria en una lista ordenada.

    Args:
        arr (list): Una lista ordenada de elementos.
        target: El elemento que se busca.

    Returns:
        int: El índice del elemento objetivo en la lista, o -1 si no se encuentra.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Ejemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
elemento_objetivo = 7
resultado = binary_search(lista_ordenada, elemento_objetivo)

if resultado != -1:
    print(f"Elemento {elemento_objetivo} encontrado en el índice {resultado}.")
else:
    print(f"Elemento {elemento_objetivo} no encontrado en la lista.")
