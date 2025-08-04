# Manejando errores
def intdiv(a, b):
    try:
        result = a // b
    except TypeError:
        print('Check operands. Some of them seems strange...')
    except ZeroDivisionError:
        print('Please do not divide by zero...')
    except Exception:
        print('Ups. Something went wrong...')

def intdiv(a, b):
    try:
        result = a // b
    except (TypeError, ZeroDivisionError):
        print('Check operands: Some of them caused errors...')
    except Exception:
        print('Ups. Something went wrong...')

intdiv(3, 0)
# intdiv(3, '0')

# Cláusulas adicionales
values = [4, 2, 7]
try:
    r = values[3]
except IndexError:
    print('Error: Index not in list')
else:
    print(f'Your wishes are my command: {r}')
finally:
    print('Have a good day!')

# Instancias de excepción
values = [4, 2, 7]
try:
    print(values[3])
except IndexError as err:
    print(f'Something went wrong: {err}')

# Elevando excepciones
def add(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    raise TypeError('Operands must be integers')

add(4, 3)
# add('x', 'y')

# Aserciones
result = -1
assert result > 0, 'Result must be positive'




