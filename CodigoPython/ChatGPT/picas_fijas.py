def picas_y_fijas(numero_secreto, intento):
    if len(str(numero_secreto)) != 4 or len(str(intento)) != 4:
        return "Los números deben tener exactamente 4 cifras."
    
    numero_secreto_str = str(numero_secreto)
    intento_str = str(intento)
    
    pica_count = 0
    fija_count = 0
    
    for i in range(4):
        if intento_str[i] == numero_secreto_str[i]:
            fija_count += 1
        elif intento_str[i] in numero_secreto_str:
            pica_count += 1
    
    resultado = {
        "PICAS": pica_count,
        "FIJAS": fija_count
    }
    
    return resultado

# Ejemplo de uso
numero_secreto = 1234
intento = 1325
resultado = picas_y_fijas(numero_secreto, intento)
print(resultado)  # Debería imprimir: {'PICAS': 1, 'FIJAS': 2}
