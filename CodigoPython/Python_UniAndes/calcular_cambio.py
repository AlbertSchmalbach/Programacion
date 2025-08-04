def calcular_cambio(cambio: int) -> int:
    monedas_500 = cambio // 500
    monedas_200 = (cambio % 500) // 200
    monedas_100 = ((cambio % 500) % 200) // 100
    monedas_50 = (((cambio % 500) % 200) % 100) // 50
    mensaje = str(monedas_500) + "," + str(monedas_200) + \
    "," + str(monedas_100) + "," + str(monedas_50)
    return mensaje

print(calcular_cambio(3500))


