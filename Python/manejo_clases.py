class Usuario:
    # atributos de clase
    username = 'Jhon Doe'
    email = 'jhondoe@mail.com'

user1 = Usuario()
user2 = Usuario()

# Atributos de instancia
print(user1.username)

# 1. Verifica si el attr existe dentro del objeto
# print(user1.__dict__)
# 2. Verifica si el attr existe dentro de la clase - solo lectura
# print(Usuario.__dict__)
# 3. Lanzar error si no existe ni en el objeto y la clase
# print(user1.usernames)
# print(Usuario.usernames)

# Apunta al mismo atributo
print(id(user1.username))
print(id(Usuario.username))

# Atributos dinamicos
user1.username = 'Harry Poter'
user1.password = '12345'
print(user1.__dict__)
print(Usuario.__dict__)
print(id(user1.username))
print(id(Usuario.username))

# print(user2.password) # Error => Este atributo es del objeto user1. No se encuentra en la clase Usuario


