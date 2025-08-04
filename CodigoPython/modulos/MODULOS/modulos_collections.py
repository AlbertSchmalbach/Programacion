from collections import Counter, defaultdict, OrderedDict, namedtuple

n = [1, 3, 5, 1, 1, 8, 10, 12]
counter = Counter(n)
print(counter)
print(Counter('Palabra'))

animales = "gato perro canario perro canario perro"
c = Counter(animales.split())
print(c)

d = defaultdict(float)  # tipo flotante por defecto
print(d['algo'])
print(d)

n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'

print(n)

Persona = namedtuple('Persona','nombre apellido edad')
p = Persona(nombre="Hector",apellido="Costa",edad=27)

print(p)

# Podemos acceder a los elementos como si fueran atributos de un objeto
print(p.nombre)
print(p.edad)

# O utilizando índices como con las tuplas clásicas
print(p[0])
print(p[-1])