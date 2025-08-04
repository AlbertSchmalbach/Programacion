from cleaner import cleaning

import math

cleaning()

# def generadora():
#     yield 1
#     yield 2
#     yield 3
    
# gen = generadora()  
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for valor in generadora():
#     print(f'Numero generado: {valor}')
    
# def generador_numeros():
#     for num in range(1,11):
#         yield num

# generador = generador_numeros() 

# while True:
#     try:
#         valor = next(generador)
#         print(f'Impresion valor generado: {valor}')
#     except StopIteration as e:
#         print('se termino de iterar el generador')
#         break
        
# EXPRESIONES GENERADORAS

# multiplicacion = (valor for valor in range(10))

# for valor in multiplicacion:
#     print(next(multiplicacion))
    
    
# suma = sum(valor for valor in range(10))
# print(f'Resultado de la suma del generador: {suma}')

# A partir de una lista

lista = ['Luz Saray', 'Paola', 'Daniela', 'Karol', 'Yuliana']

# nombres = (dato for dato in lista)

# print(next(nombres))
# print(next(nombres))
# print(next(nombres))

# Generar string a partir de lista con generador
contador = 0

def incrementar():
    global contador
    contador += 1
    return contador

generador = (f'{incrementar()}. {nombre}' for nombre in lista)
nombres = list(generador)

nombres = ', '.join(nombres)
print(nombres)

