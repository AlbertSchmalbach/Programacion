def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

# Contraseña a cifrar
password = input("Contraseña a cifrar: ")

# Valor de desplazamiento (clave de cifrado)
shift_value = int(input("clave de cifrado: "))

# Cifrar la contraseña
encrypted_password = encrypt(password, shift_value)
print("Contraseña cifrada:", encrypted_password)

# Descifrar la contraseña
decrypted_password = decrypt(encrypted_password, shift_value)
print("Contraseña descifrada:", decrypted_password)
