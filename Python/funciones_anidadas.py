from cleaner import cleaning

cleaning()

def calculadora(a, b, ope = 'sumar'):
    # Sumar
    def sumar(a,b):
        return a + b
    
    # Rstar
    def restar(a,b):
        return a - b
    
    # Multiplicar
    def mult(a,b):
        return a * b
    
    # Dividir
    def dividir(a,b):
        return a / b

    if ope == 'sumar':
        print(f'Suma: {sumar(a,b)}')
    elif ope == 'restar':
        print(f'Resta: {restar(a,b)}')
    elif ope == 'multiplicar':
        print(f'Multiplicacion: {mult(a,b)}')
    elif ope == 'division':
        print(f'Division: {dividir(a,b)}')
    else:
        print('¡Operacion invalida!')
    
    
calculadora(20, 8, 'raiz')