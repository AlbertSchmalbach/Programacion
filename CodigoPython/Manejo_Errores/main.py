# Ejercicio 1
try:
    resultado = 10/0
except:
    print('No se puede dividir por cero')

# Ejercicio 2
try:
    lista = [1, 2, 3, 4, 5]
    lista[10]
except Exception as e:
    print('Exception de tipo => ', type(e).__name__)

# Ejercicio 3
try:
    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
    colores['blanco']
except Exception as e:
    print('Exception de tipo => ', type(e).__name__)

# Ejercicio 4
try:
    resultado = 15 + "20"
except Exception as e:
    print('Exception de tipo => ', type(e).__name__)

# Ejercicio 5
try:

    elementos = [1, 5, -2]

    def agregar_una_vez(lista, element):
        if element in lista:
            raise ValueError("Error => El elemento se encuentra en la lista")
        else:
            lista.append(element)
    
    agregar_una_vez(elementos, 5)

except ValueError as v:
    print(v)
else:
    print('Funciono correctamente')
    print(elementos)


    