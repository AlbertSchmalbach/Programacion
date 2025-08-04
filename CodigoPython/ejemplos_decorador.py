def mi_decorador(funcion_decorar):
    def funcion_decoradora(*args, **kwargs):
        print('Clase de Operacion: ')
        r = funcion_decorar(*args, **kwargs)
        print('Resultado de la Operacion: ')
        return r
    return funcion_decoradora
        
@mi_decorador
def suma(a, b):
    print('*** Sumar ***')
    return a + b
    
@mi_decorador   
def resta(a, b):
    print('*** Restar ***')
    return a - b

    
print(suma(12, 8))

autenticado = True

def requiere_autenticación(funcion):
    def funcion_decorada(*args, **kwargs):
        if not autenticado:
            print("Error. El usuario no se ha autenticado")
        else:
            return funcion(*args, **kwargs)
    return funcion_decorada

@requiere_autenticación
def saludar(nombre):
    print(f"Hola {nombre}")
    
# saludar('Alberto')