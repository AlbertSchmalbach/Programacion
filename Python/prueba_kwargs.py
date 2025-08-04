def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')
        
        
describir_persona("María", color_ojos="azules", color_pelo="rubio")

