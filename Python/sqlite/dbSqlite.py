import sqlite3 as slt

def conect():
    conexion = slt.connect("miDB.db")
    cursor = conexion.cursor()
    return conexion, cursor

def crearTabla():
    conexion, cursor = conect()
    sql = """
        CREATE TABLE IF NOT EXISTS agenda(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre VARCHAR(20) NOT NULL,
        telefono VARCHAR(14) NOT NULL
        )
        """

    if cursor.execute(sql):
        print("Tabla creada")
    else:
        print("No se pudo crear la tabla")

    conexion.close()

def insertar(datos):
    conexion, cursor = conect()
    sql = """
        INSERT INTO agenda(nombre, telefono) VALUES(?, ?)
        
        """
    if cursor.execute(sql,datos):
        print("Datos guardados")
    else:
        print("No se pudieron guardar los datos")

    conexion.commit()
    conexion.close()

def consultar():
    conexion, cursor = conect()
    cursor.execute("SELECT * FROM agenda")
    for fila in cursor:
        print("Id: ", fila[0])
        print("Nombre: ", fila[1])
        print("Telefono: ", fila[2], "\n")
    conexion.cursor()

def modificar(id, telefono):
    conexion, cursor = conect()
    sql = "UPDATE agenda SET telefono="+telefono+" WHERE id="+id
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()

def borrar(id):
    conexion, cursor = conect()
    sql = "DELETE FROM agenda WHERE id="+id
    if cursor.execute(sql):
        print(f"El registro {id} fue eliminado satisfactoriamente")
    else:
        print("Registro no encontrado")

    cursor.close()
    conexion.commit()
    conexion.close()



# crearTabla()

# nombre = input("Ingresa el nombre: ")
# tel = input("Numero de telefono: ")
# datos = (nombre, tel)
# insertar(datos)

# modificar("4", "3054418062")
# borrar("8")
consultar()

