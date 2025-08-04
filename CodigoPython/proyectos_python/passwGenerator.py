import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
passw = ""

lenghtPW = int(input('Que longitud quieres para tu password: '))

for _ in range(lenghtPW):
    passw += random.choice(chars)

print(passw)