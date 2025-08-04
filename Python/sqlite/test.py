import sqlite3

# Crear base de datos
def crearBD():
    # Conectar a base de datos
    conexion = sqlite3.connect('test.db')
    # Crear cursor
    cursor = conexion.cursor()

    return conexion, cursor

# Crear una tabla 
def crearTabla():
    conexion, cursor = crearBD()
    cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER, name TEXT, age INTEGER)")
    print('Tabla creada con exito')

    conexion.close()
    
# 1. Insertar datos a la tabla
def insertarDatos(id, name, edad):
    conexion, cursor = crearBD()
    cursor.execute("INSERT INTO example VALUES (?, ?, ?)", (id, name, edad))
    print('Datos insertados correctamente!')

    conexion.commit()
    conexion.close()
    
# 2. Leer datos
def leerTabla(campos):
    conexion, cursor = crearBD()
    cursor.execute(f"SELECT {campos} FROM example")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conexion.close()

# Devuelve el numero de registros en la tabla
def contarRegistros():
    conexion, cursor = crearBD()
    cant = cursor.execute(f"SELECT COUNT(Id) FROM example")
    cant = list(cant.fetchone())
    for n in cant:
        return n
    
    conexion.close()

# 3. Modificar datos
def actualizarDatos(campo,dato, id):
    idTablas = contarRegistros()
    if id > 0 and id <= idTablas:
            conexion, cursor = crearBD()
            cursor.execute(f"UPDATE example SET {campo} = {dato} WHERE id = {id}")
            print('Datos actualizados')

            conexion.commit()
            conexion.close()
            
    else:
        print('El indentificador no existe en la tabla')

# 4. Borrar datos
def borrarDatos(id):
    idTablas = contarRegistros()
    if id > 0 and id <= idTablas:
            conexion, cursor = crearBD()
            cursor.execute(f"DELETE FROM example WHERE id = {id}")
            print('Dato eliminado de la tabla')

            conexion.commit()
            conexion.close()
    else:
        print('El indentificador no existe en la tabla')


def main():
    
    leerTabla('*')
    # insertarDatos(4, 'Luz Karime', 20)
    # actualizarDatos('age', 14, 3)
    # borrarDatos(12)
    
if __name__ == '__main__':
    main()


