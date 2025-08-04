import sqlite3

# Coneccion a base de datos
conn = sqlite3.connect("comic.db")

# Comprobar conexion
print(conn.total_changes)

# Crear manejador (cursor)
cur = conn.cursor()



# Creación de tablas
sql = """ CREATE TABLE comics (
    id_comic INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    anio_publicacion INTEGER,
    genero TEXT
)
"""

# Insertar datos a tabla
# cur.execute("INSERT INTO comics (titulo, anio_publicacion, genero) VALUES('Spider-Man', 1962, 'Superhéroes')")
# cur.execute("INSERT INTO comics (titulo, anio_publicacion, genero) VALUES('Batman: The Dark Knight Returns', 1986, 'Superhéroes')")
# cur.execute("INSERT INTO comics (titulo, anio_publicacion, genero) VALUES('Dragon Ball', 1984, 'Aventura')")

# Confirmar ingreso de datos
conn.commit()

# # Listar datos de tabla
sql = "SELECT * FROM comics"
cur.execute(sql)

filas = cur.fetchall()

for fila in filas:
    print(fila)

# # Cerrando conexion a db
conn.close()


