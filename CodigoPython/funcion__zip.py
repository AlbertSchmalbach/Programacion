num_romanos = ['I', 'II', 'III', 'IV', 'V']
num_arabigos = [1, 2, 3, 4, 5]

tipo_numero = list(zip(num_romanos, num_arabigos))

for r, n in tipo_numero:
    print(f'{r} corresponde {n}')
