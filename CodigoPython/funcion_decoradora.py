# EJEMPLO BASICO

# def funcion_decoradora(funcion_a_decorar):
#     def funcion_decorada():
#         print('Antes de ejecutar')
#         funcion_a_decorar()
#         print('Despues de ejecutar')
        
#     return funcion_decorada

# @funcion_decoradora
# def mostrar_mensaje():
#     print('Hola desde la funcion mostrar mensaje')
    
# mostrar_mensaje()

# EJEMPLO CON ARGUMENTOS VARIABLES

def funcion_decoradora(funcion_a_decorar):
    def funcion_decorada(*args, **kwargs):
        print('Antes de ejecutar')
        resultado = funcion_a_decorar(*args, **kwargs)
        print('Despues de ejecutar')
        return resultado
    return funcion_decorada

@funcion_decoradora
def sumar(a,b):
    return a + b

resultado = sumar(12, 6)
print(f'Resultado de la funcion sumar: {resultado}')
