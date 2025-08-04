from tabulate import tabulate

productos = [
    {'id':0, 'nombre': 'Papas', 'precio': 3500},
    {'id':1, 'nombre': 'Refresco', 'precio': 1200},
    {'id':2, 'nombre': 'Sandwich', 'precio': 2400}
    ]

carrito_compra = []

def menu():
    print()
    print('*** MAQUINA DE SNACK ***')
    print()
    print('Snack Disponibles: ')
    print(tabulate(productos, headers='keys'))
    print('''
    Menu: 
        1. Comprar Snack
        2. Mostrar Ticket
        3. Salir

    ''')

    opcion = input('Escoge una opcion: ')

    return opcion

def comprar_snack():

    while True:
        id_pedido = int(input('Que snack quieres (id)? '))
        for producto in productos:
            if producto.get('id') == id_pedido:
                carrito_compra.append(producto)
                print(f'Ok, snack agregado: {producto}')                    
        print()
        continuar = input('Desea añadir mas productos(Y/N): ')
        if continuar.lower() == 'n':
            break

def mostrar_ticket():
    print('**** Ticket de Venta ****')
    total_precio = 0
    for snack in carrito_compra:
        print(f'- {snack.get("nombre")} - ${snack.get("precio")}')
        total_precio += snack.get('precio')

    if total_precio != 0:
        print(f'TOTAL -> ${total_precio}')
    else:
        print('No se ha comprado ningun producto')

def main():
    
    while True:
        opcion = menu()
        
        match opcion:

            case '1':
                comprar_snack()
            case '2':
                mostrar_ticket()
            case '3':
                print('Gracias por su compra')
                break
            case __ :
                print('Opcion invalida')

if __name__ == '__main__':
    main()