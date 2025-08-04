class Persona:
    def __init__(self, name, ape):
        self.name = name
        self.ape = ape
        
    def __str__(self) -> str:
        return f'Nombre: {self.name} - Apellido: {self.ape} - Id: {hex(id(self)).upper()}'
    

persona1 = Persona('Alberto', 'Schmalbach')

print(persona1)