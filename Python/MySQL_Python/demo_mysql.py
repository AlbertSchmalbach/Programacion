import pymysql

myDB = pymysql.connect(
    host= "localhost",
    user= "root",
    passwd= "As_21048"
)

# print(myDB)

# Crear cursor
cursor = myDB.cursor()

# Crear la base de datos "BBDD_Clientes"
# cursor.execute('CREATE DATABASE BBDD_Clientes')

# Usar la base de datos "BBDD_Clientes"
cursor.execute('USE BBDD_Clientes')

# Crear la tabla "clientes"
# cursor.execute('CREATE TABLE clientes (nombre Varchar(100), direccion varchar(200))')

# cursor.execute('SHOW DATABASES')

# for b in cursor:
#     print(b)

# cursor.execute('SHOW TABLES')

# for t in cursor:
#     print(t)

# cursor.execute('ALTER TABLE clientes ADD id INT AUTO_INCREMENT PRIMARY KEY')

sql = 'INSERT INTO clientes (nombre, direccion) VALUES (%s, %s)'
# values = ('Victoria', 'Cr21C # 9 - 17 Barrio Jose Antonio Galan')
values = [
  ('Luz Saray', 'Barrio La Paz'),
  ('Misuris', 'Barrio La Paz'),
  ('Vanesa', 'C/Samaranch 156'),
  ('Antonio', 'Plaza de Mexico 16'),
  ('Enrique', 'Calle de la Rosa 36'),
  ('Javi', 'C/ Marzo 23'),
  ('Agus', 'C/ La Montaña')
]
# cursor.executemany(sql, values)

# myDB.commit()
# print(cursor.rowcount, "Registro insertado")

# cursor.execute("SELECT * FROM clientes")
# cursor.execute("SELECT * FROM clientes WHERE direccion = 'Barrio La Paz'")
cursor.execute("SELECT * FROM clientes WHERE nombre LIKE '%u%'")

for r in cursor.fetchall():
    print(r)


