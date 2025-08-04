def main():
    menu = {
    'pizza hawiana': 12000,
    'hamburgueza': 8000,
    'perro caliente': 5000,
    'gaseosa': 5000,
    'empanadas': 1500,
    'picadas': 30000,
    'jugos naturales': 7000,
    'arepas': 8000,
    'postres': 12000
}

    orden_total = 0.0

    while True:

        try:
            item = input('Ingrese un articulo de su pedido: ')
            # print(menu[item])
        except EOFError:
            break

        if item in menu:
            orden_total+= menu[item]
        elif item == 'control-D':
            print(f'El total del pedido es {orden_total:.2f}')
        else:
            print('Articulo invalido')


if __name__ == '__main__':
    main()


