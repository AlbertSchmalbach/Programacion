import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='admin', 
    database='personas_db'
)

cursor = personas_db.cursor()

# INSERTAR REGISTROS EN LA TABLA
sentencia_sql = 'INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)'
valores = ("Missel", "Bonite", 22)
cursor.execute(sentencia_sql, valores)
personas_db.commit() # Guardar cambios en DB
print('Se inserto el registro')
personas_db.close()