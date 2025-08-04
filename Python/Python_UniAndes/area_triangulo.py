import math

def area_triangulo(s1: float, s2: float, s3: float) -> float:
    s = (s1+s2+s3)/2
    resp = s * (s-s1) * (s-s2) * (s-s3)
    
    if resp >= 0:
        area = math.sqrt(resp)
        area = round(area, 1)
        return area
    else:
        print('El numero esta fuera de rango')

s1 = 9.6
s2 = 18.9
s3 = 24
solucion = area_triangulo(s1, s2, s3)
print(solucion)