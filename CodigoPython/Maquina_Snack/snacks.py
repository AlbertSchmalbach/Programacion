class Snacks:
    contador_lista = 0
    def __init__(self, lista_snacks):
        Snacks.contador_lista+=1
        self.id_snacks = Snacks.contador_lista
        # Recibimos la lista de snacks
        self.lista_snacks = lista_snacks

    def agregar_snack(self, snack):
        self.lista_snacks.append(snack)

    def __str__(self) -> str:
        snack_str = ''
        valor_factura = 0
        for snack in self.lista_snacks:
            snack_str+= snack.__str__()+'\n\n'
            valor_factura += snack.precio

        return f'''Ticket de Venta # {self.id_snacks}\n\nProductos:\n{snack_str}\nValor_Total: ${valor_factura}
        '''