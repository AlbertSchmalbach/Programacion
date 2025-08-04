# num1 = int(input('Ingrese un numero: '))
# num2 = int(input('Ingrese otro numero: '))

# try:
#     res = num1/num2
#     print(res)
# except Exception as e:
#     print('Ha habido un error de tipo: ', type(e))
# else:
#     print('Succefull!')
# finally:
#     print('Fin de la ejecucion')

# try:
#     assert num2 != 0, "No se puede dividir por cero"
#     result = num1/num2
#     print(result)
# except Exception as e:
#     print(e)


# assert() en testing
def calcula_media(lista):
    return sum(lista)/len(lista)

assert(calcula_media([5, 10, 7.5]) == 7.5)
assert(calcula_media([4, 8]) == 6)

# assert() en funciones
# Funcion suma de variables enteras
def suma(a, b):
    assert(type(a) == int)
    assert(type(b) == int)
    return a+b

# Error, ya que las variables no son int
# print(suma(3.0, 5.0))

# Ok, los argumentos son int
print(suma(3, 5))

# assert() con clases
class MiClase():
    pass

class MiOtraClase():
    pass

mi_objeto = MiClase()
mi_otro_objeto = MiOtraClase()

# Ok
assert(isinstance(mi_objeto, MiClase))

# Ok
assert(isinstance(mi_otro_objeto, MiOtraClase))

# Error, mi_objeto no pertenece a MiOtraClase
assert(isinstance(mi_objeto, MiOtraClase))

# Error, mi_otro_objeto no pertenece a MiClase
assert(isinstance(mi_otro_objeto, MiClase))