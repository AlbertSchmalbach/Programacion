# Funcion clousore
# def operacion(a,b):
#     def sumar():
#         return a + b
    
#     return sumar

# Funcion closure con lambda

def operacion(a,b):
    
    return lambda: a * b



mi_funcion_closure = operacion(12, 6)
print(f'Resultado de mi funcion closure: {mi_funcion_closure()}')

# Llamando funcion closure al vuelo
print(f'Resultado de la funcion closure al vuelo: {operacion(4, 16)()}')