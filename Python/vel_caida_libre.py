from math import sqrt



a = float()

def vel_en_caida_libre(altura: float) -> float:
    v0 = float(0)
    vf = round(float(sqrt(v0**2 + 2 * a * altura)), 2)
    return vf

print(vel_en_caida_libre(12))