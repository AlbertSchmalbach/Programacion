def sumar(a, b):
    return a + b


resultado1 = sumar(10,5)

print(f'Resultado de la funcion normal: {resultado1}')


funcion_lambda = lambda a, b : a + b

resultado2 = funcion_lambda(8, 4)

print(f'Resultado de la funcion lambda: {resultado2}')

# Sin argumentos 
my_funcion_string = lambda: 'My string'
print(f'Mi funcion sin argumento: {my_funcion_string()}')
# valores por default
my_funcion_default = lambda a= 15, b= 10: a + b
print(f'Mi funcion con valores default: {my_funcion_default()}')

# funcion con argumentos *args y **kwargs
my_funcion_args = lambda *args, **kwargs : len(args) + len(kwargs)
my_dict = {'a':5, 'b':10}
print(f'Mi funcion con valores args: {my_funcion_args((1,2,3), my_dict)}')


