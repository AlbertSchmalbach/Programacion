# DATOS DE ENTRADA
# nombre
# apellido
# gestor de correo

# DATOS DE SALIDA
# nombre.apellido+@gestor_correo.com

print('*** Bienvenido al sistema Generador de Email ***')

nombre = input('Cual es tu nombre?: ')
ape = input('Cual es tu apellido?: ')
gestor_correo = input('Con que gestor de correo lo quieres?: ')

correo_generado = f'{nombre.lower()}{ape.lower()}@{gestor_correo}.com'

print(f'''
    Tu nuevo email generado por el sistema es:
        {correo_generado}
        *** Felicidades ***
''')