words = 'Curso profesional de Python'

print(words)
print('P' in words)
print(len(words))

rebanada = words[:17]
print(rebanada)

print('Curso' in words)

# split and join
frutas = 'Pera Piña Sandia Uva Mora'
print(frutas.split(' '))

cursos = ['Python', 'Java', 'Ruby']
print(', '.join(cursos))