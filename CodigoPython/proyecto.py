import os, cleaner

CARPETA = 'contacto/'
EXTENSION = '.txt'

cleaner.cleaning()

# contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    
    # Funcion para crear directorio
    crear_directorio()

    # Mostrar menu
    mostrar_menu()

    # Preguntar al usuario la accion a realizar
    preguntar = True

    while preguntar:
        opcion = input('Seleccione una opcion: ')
        opcion = int(opcion)

        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 6:
            print('Saliendo...')
            preguntar = False
        else:
            print('¡Opcion invalida!...intente de nuevo')

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: ')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n Eliminado correctamente \r\n')
    except:
        print('No existe es contacto')

def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')

    # Reinicar la app
    app()

def mostrar_contacto():
    print()
    archivo = os.listdir(CARPETA)
    archivo_txt = [file for file in archivo if file.endswith(EXTENSION)]

    for files in archivo_txt:
        with open(CARPETA + files) as contacto:
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    app()

def editar_contacto():
    # print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    # Revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

             # resto campos
            nombre_contacto = input('Agrega el nuevo Nombre: \r\n')
            telefono_contacto = input('Agrega el nuevo Telefono: \r\n')
            categoria_contacto = input('Agrega la nuevo Categoria: \r\n')

             # instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            archivo.close()

            # Renombrar archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            # Mensaje de exito
            print('\r\n ¡Cambios guardados correctamente! \r\n')
    else:
        print('Este contacto no existe')

    cleaner.cleaning()

    app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del Contacto: \r\n')

    # existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION)
    existe = existe_contacto(nombre_contacto)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            # resto campos
            telefono_contacto = input('Agregar el telefono: \r\n')
            categoria_contacto = input('Categoria contacto: \r\n')

            # instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            archivo.close()
            # mensaje de exito
            print('\r\n ¡Contacto agregado satisfactoriamente! \r\n')
    else:
        print('¡Atencion!... Este contacto ya existe')

    cleaner.cleaning()

    app()

def mostrar_menu():
    print('Seleccione del Menu lo que desea hacer: ')
    print('(1) Agregar nuevo Contacto')
    print('(2) Editar Contacto')
    print('(3) Ver Contacto')
    print('(4) Buscar Contacto')
    print('(5) Eliminar Contacto')
    print('(6) Salir')

def crear_directorio():
   if not os.path.exists(CARPETA):
    #    Crear diretorio
       os.makedirs(CARPETA)
       print('¡Carpeta creada con exito!')

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()