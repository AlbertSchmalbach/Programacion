from producto import Producto

def productos_en_stock():
    productos = [
    {'nombre': 'Manzana', 'valor': 0.5, 'cantidad': 100},
    {'nombre': 'Banana', 'valor': 0.3, 'cantidad': 150},
    {'nombre': 'Naranja', 'valor': 0.4, 'cantidad': 200},
    {'nombre': 'Pera', 'valor': 0.6, 'cantidad': 80},
    {'nombre': 'Uva', 'valor': 1.2, 'cantidad': 50},
    {'nombre': 'Melón', 'valor': 3.0, 'cantidad': 20},
    {'nombre': 'Sandía', 'valor': 4.0, 'cantidad': 15},
    {'nombre': 'Piña', 'valor': 2.5, 'cantidad': 30},
    {'nombre': 'Mango', 'valor': 1.5, 'cantidad': 40},
    {'nombre': 'Fresa', 'valor': 2.0, 'cantidad': 60}
    ]

    return productos

productos = productos_en_stock()


for p in productos:
    nombre = p['nombre']
    valor = p['valor']
    cant = p['cantidad']

    carrito = Producto(nombre, valor, cant)

    if carrito.get_cantidad() > 100:
        print(nombre)