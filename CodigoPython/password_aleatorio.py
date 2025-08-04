import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Longitud de las contraseñas
password_length = 10

# Número de contraseñas a generar
num_passwords = 3

# Generar las contraseñas
passwords = [generate_random_password(password_length) for _ in range(num_passwords)]

# Mostrar las contraseñas generadas
for i, password in enumerate(passwords, start=1):
    print(f"Contraseña {i}: {password}")
