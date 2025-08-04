# if simple
if True:
    print('Condicional simple')

# if compuesto   
valor = 12

if valor > 10:
    print('El valor es mayor a 10')
else:
    print('El valor no es mayor a 10')
    
# if anidado

# if con varias condiciones
profesion = 'programer'

if profesion == 'ingeniero':
    print('Eres un buen ingeniero')
elif profesion == 'programer':
    print('Genial!... Somos colegas')
elif profesion == 'chofer':
    print('Eres un buen chofer')
else:
    print('Tienes otra profesion')
    
# match
planeta = "Tierra"

match planeta:
    case "Marte":
        print(f" {planeta} planeta cercano a la tierra")
    case "Saturno":
        print(f"{planeta} es el segundo planeta mas grande")
    case "Tierra":
        print(f"La {planeta} es el unico planeta con vida comprobada")
    case "Jupiter":
        print(f"{planeta} es el planeta mas grande del sistema solar")
    case _:
        print(f"{planeta} no es un planeta del sistema solar")

# ternario
edad = 25
mayor_edad = 'Si es mayor de edad' if edad >= 18 else 'Es menor de edad'
print(mayor_edad)