# clourser
def sumar(num1):

    def operar(num2):
        return num1 + num2
    
    return operar

suma = sumar(12)

func = suma(18)

print(func)

# decoradores
def decorador(func):

    def mensaje(name):
        return f'Hola, como te va {func(name)}'
        
    return mensaje


@decorador
def nombrarPersona(name):
    return name

print(nombrarPersona('Luz Saray'))