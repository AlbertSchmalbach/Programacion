def es_divisible(n: int, d: int) -> int:
    try:
        if n % (2*d) == 0:
            return 2
        elif n % d == 0 and n % (2*d) != 0:
            return 1
        else:
            return 0
    except ZeroDivisionError:
        return 0


resultado = es_divisible(3, 0)

print(resultado)
