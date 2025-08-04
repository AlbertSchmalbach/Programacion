rols = ['admin', 'user1', 'user2']
person = ['Albert', 'Paola', 'Mario']

response = list(zip(rols, person))

for user in response:
    print(user)