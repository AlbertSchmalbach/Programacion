import sqlite3
import os

# Crear base de datos
def crearBD():
    # Conectar a base de datos
    conexion = sqlite3.connect('curso.db')
    # Crear cursor
    cursor = conexion.cursor()

    return conexion, cursor

# Crear una tabla 
def crearTabla():
    conexion, cursor = crearBD()
    cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, notas INTEGER)")
    print('Tabla creada con exito')

    conexion.close()

# Limpiar consola
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
# 1. Insertar datos a la tabla
def insertarDatos(nombre, nota):
    conexion, cursor = crearBD()
    cursor.execute("INSERT INTO alumnos VALUES (NULL, ?, ?)", (nombre, nota))
    print('Datos insertados correctamente!')

    conexion.commit()
    conexion.close()   
# 2. Leer datos
def leerTabla():
    clear()
    conexion, cursor = crearBD()
    cursor.execute("SELECT * FROM alumnos")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conexion.close()

def modificarRegistro(id):
    conexion, cursor = crearBD()
    campo = input('Digite el campo a modificar: ')

    if campo == 'nombre':
        valor = str(input('Actualizar valor nombre: '))
        cursor.execute(f"UPDATE alumnos SET nombre = '{valor}' WHERE id={id}")
    else:
        valor = int(input('Actualizar nota: '))
        cursor.execute(f"UPDATE alumnos SET notas = {valor} WHERE id={id}")

    print('¡El registro fue actualizado con exito!')
    print()

    conexion.commit()
    conexion.close()

    leerTabla()

def eliminarRegistro(id):
    conexion, cursor = crearBD()

    cursor.execute(f"DELETE FROM alumnos WHERE id = {id}")

    print('Registro eliminado')
    print()

    conexion.commit()
    conexion.close()

    leerTabla()

def menu():

    print()
    print('*** SISTEMA DE NOTAS ALUMNOS ***'.center(50, '*'))
    print()
    print("1. Agregar nuevos usuarios")
    print("2. Listar alumnos y notas")
    print("3. Editar usuarios")
    print("4. Eliminar usuarios")
    print("5. Salir")
    print()


def main():

    while True:

        menu()

        opcion = input("Seleccione una opción (1|2|3|4|5): ")

        match opcion:

            case '1':
                print('INSERTANDO DATOS A LA TABLA')
                print()
                nombre = input('Nombre del Alumno: ')
                nota = int(input('Ingrese la nota: '))
                insertarDatos(nombre, nota)
            
            case '2':
                print('REGISTRO DE LA TABLA')
                print()
                leerTabla()

            case '3':
                print('EDICION REGISTRO')
                print()
                id = int(input('Ingrese el Id del registro: '))
                modificarRegistro(id)

            case '4':
                print('ELIMINANDO REGISTRO DE LA TABLA')
                print()
                id = int(input('Ingrese el Id del registro: '))
                eliminarRegistro(id)
            
            case '5':
                print("Saliendo del programa...")
                break

            case _:
                print("Opción no válida. Por favor, seleccione 1, 2, 3, 4 o 5.")


if __name__ == '__main__':
    main()
