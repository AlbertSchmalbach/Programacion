from typing import Tuple, Dict, List, Set

# Definir variables con su tipo
name: str = 'Albert'
age: int = 33
height: float = 1.74
is_dev: bool = True

# Definir el tipo de retorno en una función
def sum(num1: int, num2: int) -> int:
    return num1 + num2

# Definir tipos de datos complejos
tupla: Tuple = (0, 1, 2, 3)
diccionario: Dict = {'name': 'Alber'}
lista: List = [0, 1, 2, 3]
conjunto: Set = {0, 1, 2, 3}