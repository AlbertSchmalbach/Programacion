f_nac = input('Fecha de Nacimiento: ')

F_nac_str = list(str(f_nac))

f_nac_int = []

for n in F_nac_str:
    f_nac_int.append(int(n))
    
digit_life = str(sum(f_nac_int))

if len(digit_life)> 1:
    digit_life = list(digit_life)
    list_digit_life = []
    for n in digit_life:
        list_digit_life.append(int(n))
        
    digit_life = sum(list_digit_life)
    
    print(digit_life)
    
else:
    print(digit_life)
    
        
        
    
