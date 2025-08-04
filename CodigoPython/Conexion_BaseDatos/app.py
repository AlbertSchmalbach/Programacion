import pymysql
from decouple import config

DROP_TABLE_USERS = """DROP TABLE IF EXISTS users"""

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

users = [
    ('Luz Saray', 'luzSa123', 'luzatenciam@gmail.com'),
    ('Misuris Atencia', 'misu12345', 'misuatencia@gmail.com'),
    ('Maria Fernanda', 'mafer12345', 'mariafer12@gmail.com'),
    ('Nazly Silvera', 'nazly12345', 'nazlysilvera@gmail.com'),
    ('user', 'user12345', 'user12345@gmail.com')
]


if __name__ == '__main__':

    try:
        connect = pymysql.Connect(
            host='127.0.0.1', 
            port=3306, 
            user=config('USER_MYSQL'), 
            passwd=config('PASSWORD_MYSQL'), 
            db=config('DB_MYSQL')
            )

        with connect.cursor() as cursor:

            cursor.execute(DROP_TABLE_USERS)
            cursor.execute(USERS_TABLE)

            # 1. Insertar registro

            query = "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)"
            # values =('Luz Saray', 'luzSa123', 'luzatenciam@gmail.com')

            # Insertar un solo registro

            # cursor.execute(query, values)

            # Insertar multiples registros

            # 1. forma
            # for user in users:
            #     cursor.executemany(query, user)
            
            # 2. forma
            cursor.executemany(query, users)
            connect.commit()

            # 2. Consultar Registro
            query = "SELECT id, username, email FROM users"
            rows = cursor.execute(query)

            # Listar todos
            # print(cursor.fetchall())

            # for user in cursor.fetchall(): 
            # for user in cursor.fetchmany(2): # Solo los indicados.
            # user = cursor.fetchone() #Solo 1
            # print(user)

            # 3. Actualizar Registro
            query = "UPDATE users set username = %s WHERE id = %s"
            values = ("Luciana", 5)

            # cursor.execute(query, values)
            # connect.commit()

            # 4. Eliminar Registro
            query = "DELETE FROM users WHERE id = %s"
            value = (5,)

            cursor.execute(query, value)
            connect.commit()
            
        print("Conexion exitosa!")
    
    except Exception as e:
        print("No fue posible completar la operacion.")
        print(f"Error de tipo: {e}")

    finally:
        connect.close()
        print("Conexion finalizada de forma exitosa!")