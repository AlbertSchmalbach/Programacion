# Definir variables con su tipo
from ast import Dict, List, Set, Tuple


name: str = 'Albert'
age: int = 35
height: float = 1.72
is_dev: bool = True

print(type(name))
print(type(age))
print(type(is_dev))

# Definir el tipo de retorno en una función


def sum(num1: int, num2: int) -> int:
    return num1 + num2


print(sum(12, 18))

# Definir tipos de datos complejos
tupla: Tuple = (4, 8, 12)
diccionario: Dict = {'name': 'Albert'}
lista: List = [12, 4, 10, 5, 20]
conjunto: Set = {0, 45, 10, 35, 8}

print(type(diccionario))
print(type(lista))