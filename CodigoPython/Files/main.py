file = open('data.txt', 'r')

# for dato in file:
#     print(dato)
    
# print(file.readline())
# print()

file.seek(0) #Esta función permite situar el «puntero de lectura» en cualquier byte del fichero

# for dato in file:
#     print(dato)
    
# Enumerando líneas
for line, cod in enumerate(file, start=1):
    print(f'Cod:{line} - {cod}')

# Escritura en un fichero
f = open('codes_canary.txt', 'w')

# canary_iata = ('TFN', 'TFS', 'LPA', 'GMZ', 'VDE', 'SPC', 'ACE', 'FUE')
canary_iata = ('TFN\n', 'TFS\n', 'LPA\n', 'GMZ\n', 'VDE\n', 'SPC\n', 'ACE\n', 'FUE\n')

for code in canary_iata:
    # f.write(code + '\n')
    # f.write('\n'.join(canary_iata)
    f.writelines(canary_iata)
    
f.close()
