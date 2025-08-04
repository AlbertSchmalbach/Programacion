from tabulate import tabulate

almacen = []
cod = 100
cantidad_inicial = 0

def menu():

    print()
    print('*** SISTEMA DE PRODUCTOS ***'.center(50, '*'))
    print()
    print("1. AGREGAR PRODUCTO")
    print("2. LISTAR PRODUCTO")
    print("3. VENTA PRODUCTO")
    print("4. EDITAR PRODUCTO")
    print("5. ELIMINAR PRODUCTO")
    print("6. SALIR")
    print()

def agregar_producto():
    
    global cod
    global cantidad_inicial

    while True: 
        cod += 1
        productos = {'Codigo': cod}
        nombre_producto = input('Ingrese el nombre del producto: ').capitalize()
        productos['Nombre'] = nombre_producto

        precio_producto = float(input('Precio del producto: '))
        productos['Precio'] = precio_producto

        cantidad_almacen = int(input('Cantidad inicial: '))
        cantidad_inicial = cantidad_almacen
        productos['Stock_Inicial'] = cantidad_almacen
        productos['Cantidad_Vendida'] = 0
        productos['Venta_Total'] = 0
        productos['Stock_Final'] = 0
        almacen.append(productos)

        print()

        continuar = input('Desea añadir mas productos(SI/NO): ')

        if continuar == 'no':
            break
        
        print()
 
def listar_producto():
    print()
    print(tabulate(almacen, headers='keys'))

def venta_producto(codigo):

    global cantidad_inicial

    try:
        
        for item in almacen:
            
            if item['Codigo'] == codigo:
                print(f'Articulo seleccionado: {item["Nombre"]}')
                item['Cantidad_Vendida'] = int(input(f'Cantidad de {item["Nombre"]} a vender: '))
                item['Venta_Total'] = item['Precio'] * item['Cantidad_Vendida']
                item['Stock_Final'] = cantidad_inicial - item['Cantidad_Vendida']
                cantidad_inicial = item['Stock_Final']
            
                if item['Stock_Final'] < 0:
                    print(f'Lo sentimos, las {item["Nombre"]} se han agotado')
                else:
                    print('Producto vendido con exito!')
                
    except:
        print('El codigo no se encuentra asociado a ningun producto')

def editar_producto(codigo):

    try:
        for item in almacen:
            if item['Codigo'] == codigo:
                print(f'Articulo seleccionado: {item["Nombre"]}')
                item['Precio'] += float(input('Valor Incremento: '))
                print('Producto editado con exito!')    
    except:
        print('El codigo no se encuentra asociado a ningun producto')

def eliminar_producto(codigo):
    try:
        for item in almacen:
            if item['Codigo'] == codigo:
                print(f'Articulo Eliminado: {item["Nombre"]}')
                item.clear()
                print('Producto eliminado con exito!') 
    except:
        print('El codigo no se encuentra asociado a ningun producto')


def main():
    
    while True: 

        menu()

        opcion = input("Seleccione una opción (1|2|3|4|5|6): ")

        match opcion:

            case '1':
                agregar_producto()
            case '2':
                listar_producto()
            case '3':
                codigo = int(input('Digite el codigo del producto a vender: '))
                venta_producto(codigo)
            case '4':
                codigo = int(input('Digite el codigo del producto a editar: '))
                editar_producto(codigo)
            case '5':
                codigo = int(input('Digite el codigo del producto a eliminar: '))
                eliminar_producto(codigo)
            case '6':
                print("Ha salido con exito")
                break

if __name__ == '__main__':
    main()