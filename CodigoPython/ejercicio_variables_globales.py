contador = 0

def mostrar_contador():
    print(contador)
    
    
def modificar_contador(n):
    global contador
    
    contador = n
    
    
modificar_contador(10)
mostrar_contador()