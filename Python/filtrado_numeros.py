numeros_aleatorios = [4, 8, 15, 16, 23, 42, 2, 7, 11, 13, 17, 19]
print(numeros_aleatorios)

def is_pair(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False

filtro = filter(is_pair, numeros_aleatorios)

for n in filtro:
    print(n, end=' ')