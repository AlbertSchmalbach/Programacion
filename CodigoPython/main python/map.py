print(True if 0 >= 0 else False)

for x in (el * 2 for el in range(5)):
    print(x)

def foo(x, f):
    return f(x)
 
print(foo(9, lambda x: x ** 0.5))

short_list = ['mython', 'python', 'cayó', 'en', 'el', 'piso']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)

short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)