num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

try:
    if num2 == 0:
        raise ZeroDivisionError("No se puede dividir por 0")
        result = num1/num2
        print(result)
        
except ZeroDivisionError as err:
    print(err)
else:
    print("Succesfull!")
finally:
    print("Ejecucion finalizada")
