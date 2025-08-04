# https://www.bytebank.com/cambio?monedaOrigen=usd&monedaDestino=cop&cantidad=100

url = "www.bytebank.com/cambio?monedaOrigen=usd"
print(url)

url_base = url[0:23]
print(url_base)  # Imprimirá "www.bytebank.com/cambio"
url_parametros = url[24:41] # Imprimira "monedaOrigen=usd&monedaDestino=cop&cantidad=100"
print(url_parametros)

url = 'https://www.bytebank.com/cambio?monedaOrigen=usd&monedaDestino=cop&cantidad=100&operacion=venta'
url.find('?')
indice_interrogacion = url.find('?')
base_url = url[:indice_interrogacion]
parametros_url = url[indice_interrogacion + 1:]
print(base_url) # Imprimirá "www.bytebank.com/cambio"
print(parametros_url) # Imprimira "monedaOrigen=usd&monedaDestino=cop&cantidad=100&operacion=venta'"

parametro_busqueda = 'operacion'
indice_parametro = parametros_url.find(parametro_busqueda)
indice_valor = indice_parametro + len(parametro_busqueda) + 1

indice_and = parametros_url.find('&',indice_valor)
if indice_and == -1:
  valor = parametros_url[indice_valor:]
else:
  valor = parametros_url[indice_valor:indice_and]
print(valor)

# ReEx (Expresiones regulares)
import re

contacto = 'Mi numero de contacto es 320-452-4560'
patron = re.compile('[0-9]{3}-?[0-9]{3}-?[0-9]{4}')

busqueda = patron.search(contacto)

if busqueda:
  print(busqueda.group())