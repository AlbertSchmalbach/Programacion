import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='admin', 
    database='personas_db'
)

cursor = personas_db.cursor()

sentencia_slq = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores = ('Yulianis', 'Mauris', 16, 5)
cursor.execute(sentencia_slq, valores)
personas_db.commit()
print('Se ha actualizado el registro')
personas_db.close()