def my_primer_decorador(function):
    def funcion_de_retorno(nombre):
        print('Cargando...')
        function(nombre)
        print('Proceso finalizado. 😎')

    return funcion_de_retorno

@my_primer_decorador
def saludo(nombre):
    print(f'Hola {nombre}')
   
if __name__ == "__main__":  
    saludo('Luz Saray')