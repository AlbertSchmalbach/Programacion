class Contacto:
    def __init__(self, nombre, celular, email, cargo):
        self.nombre = nombre
        self.__celular = celular
        self.__email = email
        self.cargo = cargo

    def mostrar_contacto(self):
        print(f'''
            Informacion de Contacto:
            Nombre  => {self.nombre}
            Celular => {self.__celular}
            Correo  => {self.__email}
            Cargo   => {self.cargo}
        ''')


contacto1 = Contacto('Paul', '3002543660', 'paul@mail.com', 'gerente')
contacto2 = Contacto('Dayan', '3202805660', 'dayan@mail.com', 'asistente')
contacto1.__celular = '3054785124'
contacto1.mostrar_contacto()
