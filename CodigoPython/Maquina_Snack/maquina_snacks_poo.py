from snack import Snack
from snacks import Snacks

snack1 = Snack('Papas', 3500)
snack2 = Snack('Refresco', 1800)
snack3 = Snack('Sandwich', 2400)

# print(snack1)
# print(snack2)

lista_snacks = [snack1, snack2]

orden = Snacks(lista_snacks)
orden.agregar_snack(snack3)

print(orden)