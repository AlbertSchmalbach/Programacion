import random

def generate_passwords(phrase1, phrase2, phrase3, num_passwords, length):
    phrases = [phrase1, phrase2, phrase3]
    passwords = []

    for _ in range(num_passwords):
        password = ''.join(random.choice(random.choice(phrases)) for _ in range(length))
        passwords.append(password)
    
    return passwords

# Frases para construir las contraseñas
phrase1 = "Luz Saray Atencia"
phrase2 = "El amor es la llama de Jah"
phrase3 = "Nuevo mundo"

# Número de contraseñas a generar
num_passwords = 5

# Longitud de las contraseñas
password_length = 12

# Generar las contraseñas
passwords = generate_passwords(phrase1, phrase2, phrase3, num_passwords, password_length)

# Mostrar las contraseñas generadas
for i, password in enumerate(passwords, start=1):
    print(f"Contraseña {i}: {password}")
