num1 = '5'
num2 = 0

try:
    x = num1 / num2
except ZeroDivisionError as err:
    print('No puedes dividir un número entre 0')
except TypeError as err:
    print('Los dos valores deben ser númericos')
except Exception as err:
    print('Error desconocido')
finally:
    print('Codigo ejecutado')