from cleaner import cleaning

cleaning()

# Listas

serpList = ["Boa", "Piton", "Culebra venenosa", "Víbora Rayada", "Piton"]

# metodos listas

# 1. append
serpList.append('Cobra')
# 2. copy
serpList2 = serpList.copy()

print('1. ', serpList2)
# 3. count 
print('2. ',serpList.count('Piton'))
# 4. insert
serpList.insert(1, 'Coral')
print('3. ',serpList)
# 5. reverse
li = [1, 2, 3, 4, 5]
li.reverse()
print('4. ', li)
# 6. remove
serpList.remove('Piton')
print('5. ',serpList)
# 7. sort
serpList.sort()
print('6. ',serpList)
# 8. pop
serpList.pop()
print('7. ',serpList)
# 9. extend
serpList.extend(["Mapana", "barba amarilla"])
print('9. ',serpList)
# 10. index
print('10. ',serpList.index('Coral'))
# 11. clear
serpList.clear()
print('11. ',serpList)

# diccionarios
pass

# conjuntos
pass

# MISELANEO PYTHON

# mayor y menor numero de una lista
def max_min(lst):
    max_num = lst[0]
    min_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return (max_num, min_num)

print(max_min([4, 2, 9, 1, 7]))

# trasnponer lista multidimensional

m = [[1, 2, 3], [4, 6, 8]]

new_m = [[m[j][i] for j in range(len(m))]for i in range(len(m[0]))]

print(new_m)

import numpy as np

print(np.transpose(m))

