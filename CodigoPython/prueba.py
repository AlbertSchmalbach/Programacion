import math
from random import randint
import platform

def print_random_numbers(count, start, end):
    print("Números aleatorios:", end=' ')
    for _ in range(count):
        print(randint(start, end), end=' ')
    print()

def compare_e_and_pow():
    result = math.e != math.pow(2, 4)
    print(f"¿math.e es diferente de 2^4?: {int(result)}")

def print_platform_info():
    print(f"Sistema operativo: {platform.system()}")
    print(f"Versión: {platform.version()}")

if __name__ == "__main__":
    print_random_numbers(2, 1, 2)
    compare_e_and_pow()
    print_platform_info()
