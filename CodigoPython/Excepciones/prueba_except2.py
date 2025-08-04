def divide():

    try:
    
        ope1 = float(input('Introduce el primer valor: '))
        ope2 = float(input('Introduce el segundo valor: '))
        print(f"El resultado de la division es: {ope1/ope2}")

    except ValueError:
        print("Ha introducido un tipo de dato incorrecto")

    except ZeroDivisionError:
        print("La division por 0 no es valida")

    except Exception as e:
        print(f"error de tipo: {e}")
        
    finally:
        print("Calculo realizado")

divide()