# DATOS DE ENTRADA:
# Pedir nombre
# Pedir apellido
# Pedir año de nacimiento

# DATOS DE SALIDA:
# Hola [nombre], habitante de ciudad gotica!
    # Tu nuevo numero de identificacion (ID) generado por sistema es:
    # 2 primeros caracteres del nombre, apellido, 2 ultimos del año de nacimiento y un numero aleatorio de 4 digitos
    # Felicidades

# SOLUCION
import random

print('*** Sistema de Generador ID unico ***'.center(3, '*'))
# datos de entrada
name = input('Cual es tu nombre?: ')
lastname = input('Cual es tu apellido?: ')
age_born = input('Cual es tu año de nacimiento (YYYY)?: ')

# proceso
name2 = name[0:2].upper()
lastname2 = lastname[0:2].upper()
age_born2 = age_born[2:4]

num_aleatorio = random.randint(0, 9999)

id_unico = f'{name2}{lastname2}{age_born2}{num_aleatorio}'

print(f'''
    Hola {name}, habitante de ciudad gotica!
        Tu nuevo numero de identificacion (ID) generado por sistema es:
        {id_unico}
        Felicidades!    
''')
