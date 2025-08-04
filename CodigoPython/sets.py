conjunto = {1,2,3,4,5}
conjunto = set([1,2,3,4,5])

# print(conjunto, type(conjunto))

conjunto.add(7)

# print(conjunto, type(conjunto))

conjunto2 = {8,9,10, 2,3}

conjunto.update(conjunto2)

# print(conjunto)

# Union()
ojos_azules = {'Albert', 'Maria', 'Dayan'}
ojos_Cafe = {'Daniela', 'Carolina', 'Rosa', 'Esperanza', 'Manuel'}
tes_blanca = {'Albert', 'Carolina', 'Maria', 'Dayan', 'Daniela'}
tes_Morena = {'Rosa', 'Esperanza', 'Manuel'}

# Morenos ojos cafe
print(tes_Morena.union(ojos_Cafe))

# intersection()
print(ojos_azules.intersection(tes_blanca))

# difference()
print(tes_blanca.difference(ojos_azules))

# symmetric_difference()
print(tes_Morena.symmetric_difference(ojos_Cafe))

# subset() => si los elementos del primer set se encuentran en el segundo set
print(ojos_azules.issubset(tes_blanca))

# issuperset() => si los elementos del primer set se encuentran en el segundo set
print(ojos_azules.issuperset(tes_blanca))

# isdisjoint() => los elementos del primer set no se encuentran en el segundo
print(tes_Morena.isdisjoint(ojos_azules))