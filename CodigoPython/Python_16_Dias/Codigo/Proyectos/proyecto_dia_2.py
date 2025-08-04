name = input("Por favor dime tu nombre?: ")
ingresos_ventas = float(input("Cuánto han vendido en este mes?: "))
porcentaje_comision = 13/100

comision = round(ingresos_ventas * porcentaje_comision, 2)

print(f"Hola {name} tus comisiones este son de ${comision}")


