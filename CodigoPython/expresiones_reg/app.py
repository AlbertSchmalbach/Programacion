import re


text = 'Estaré disponible en el +3043830143 el lunes por la tarde'

text2 = '''
Datos de contacto:
  - Marketing: Rubén López (+3207543181)
  - Ventas: Sara Mondragón (+3051788902)
  - Desarrollo: Eva Blasco (+3142131262)
© Saturno Desarrollos de Software
'''

regex = r'\+?\d{3}\d{7}'

# Por grupos
# regex = r'\+?(\d{3})(\d{7})' # Captura posiciones
regex = r'\+?(?P<prefix>\d{3})(?P<number>\d{7})' # Captura nominal
# Búsqueda simple
m = re.search(regex, text, re.IGNORECASE)

# Búsqueda múltiple
n = re.findall(regex, text2)

print(m)
print(m[0])
# print(m.span(0))
# print(m[1])
# print(m[2])

print(n)

# Separar
regex = r'[.,]'
regex = r'([.,])' # Capturar
num1 = re.split(regex, '3.14')
num2 = re.split(regex, '3,14')

print("Parte entera: {}".format(num1[0]))
print("Parte decimal: {}".format(num2[1:3]))

# Reemplazar
name = 'Alberto Schmalbach'

regex = r'(\w+) +(\w+)'
# regex = r'(?P<name>\w+) +(?P<surname>\w+)'
# repl = r'\2, \1'
# repl = r'\g<surname>, \g<name>'
# inverName = re.sub(regex, repl, name)
inverName = re.sub(regex, lambda m: f'{m[2].upper()}, {m[1].title()}', name)
print(inverName)

# Casar o Coincidir
regex = r'\d{8}[A-Z]'
text = '54632178Y'
caso1 = re.fullmatch(regex, text)
text = '87896532$'
caso2 = re.fullmatch(regex, text)

print(caso1)
print(caso2)


def check_id_card(text: str) -> None:
    REGEX = r'(\d{8})([A-Z])'
    if m := re.fullmatch(REGEX, text):
        print(f'{text} es un DNI válido')
        print(f'N: {m[1]}  CC: {m[2]}')
    else:
        print(f'{text} no es un DNI válido')
        
check_id_card('54632178Y')
check_id_card('87896532$')