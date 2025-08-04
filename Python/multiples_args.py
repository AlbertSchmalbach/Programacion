def suma(*args):
    resultado = sum(args)
    return resultado


def mis_cursos(**kwargs):
    for k, v in kwargs.items():
        print(f'El curso {k}, tiene un valor de {v}$ pesos')



total_suma = suma(25, 18, 250)

print(total_suma)
mis_cursos(Python=50000, Java=80000)