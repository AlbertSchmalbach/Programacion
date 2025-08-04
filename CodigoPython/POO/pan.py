class Pan:

    def __init__(self, nombre, categoria, precio):
        # protected(_) private(__)
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio # private

    def informacion_pan(self):
        print(f'Nombre: {self.nombre} - Categoria: {self.categoria} - Precio: {self.precio}')

    # GETTER Y SETTER
    # def get_precio(self):
    #     print(self.__precio)
    
    # def set_precio(self, precio):
    #     self.__precio = precio

# 1. instanciando un objeto de la clase Pan:

# ocanero = Pan('Ocañero', 'dulce', 300)
# ocanero.informacion_pan()
# mantequilla = Pan('Mantequilla', 'sal', 300)
# mantequilla.set_precio(480) # No permite modificacion
# mantequilla.informacion_pan()
# queso = Pan('Queso', 'sal', 500)
# queso.informacion_pan()

# 2. Herencia de la clase Pan:

# class Pan_Especial(Pan):
#     def __init__(self, nombre, categoria, precio):
#         super().__init__(nombre, categoria, precio)


# especial1 = Pan_Especial('Piñita', 'Azucarado', 500)

# especial1.informacion_pan()

# 3. Polimorfismo

class Pan_Especial(Pan):
    def __init__(self, nombre, categoria, precio, tienda):
        super().__init__(nombre, categoria, precio)
        self.tienda = tienda

    def informacion_pan(self):
        print(f'Nombre: {self.nombre} - Categoria: {self.categoria} - Precio: {self.precio} - Tienda: {self.tienda}')


especial2 = Pan_Especial('Pizza', 'Caramelado', 800, 'centro')

especial2.informacion_pan()


