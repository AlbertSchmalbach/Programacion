def funcion_externa():
    variable_local_externa = 'Soy la variable local externa'
    
    def funcion_anidada():
        variable_local_anidada = 'Soy la variable local anidada'
        
        nonlocal variable_local_externa
        
        variable_local_externa = 'Nuevo valor variable local externa'
        
    funcion_anidada()
    
    print(f'Valor variable local externa: {variable_local_externa}')
    
    
funcion_externa()