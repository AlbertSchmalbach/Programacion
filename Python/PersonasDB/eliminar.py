import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='admin', 
    database='personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valor = (9,)
cursor.execute(sentencia_sql, valor)
personas_db.commit()
print('Se elimino el registro')
personas_db.close()