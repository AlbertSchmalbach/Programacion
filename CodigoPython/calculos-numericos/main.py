from modulos_aritmeticos import suma, multiplicacion
from modulos_estadisticos import media, mediana, moda

def run():
    # adicion = suma(12, 5, 10)
    # print(adicion)
    # mult = multiplicacion(40,5)
    # print(mult)

    datos = [10, 20, 30, 40, 50, 20, 20, 20]
    print("Promedio:", media(datos))  # Debería imprimir 30.0
    print("Mediana:", mediana(datos))    # Debería imprimir 30

if __name__ == '__main__':
    run()


