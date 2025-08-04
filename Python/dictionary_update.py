from cleaner import cleaning

cleaning()

a = {'key1': 1, 'key2': 2}
b = {'key3': 3, 'key4': 4}

a |= b

print(a)