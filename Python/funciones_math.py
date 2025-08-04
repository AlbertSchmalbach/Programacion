import math

numero = 12.47
p = [4, 12, 11, 10]
q = [12, 7, 25]
print(f"round: {round(numero)}")
print(f"ceil: {math.ceil(numero)}")
print(f"floor: {math.floor(numero)}")
print(f"pow: {math.pow(numero, 2)}")
print(f"pow2: {numero**2}")
print(f"sqrt: {math.sqrt(numero)}")
print(f"sqrt2: {numero**0.5}")
print(f"{math.sumprod(p, q)}")