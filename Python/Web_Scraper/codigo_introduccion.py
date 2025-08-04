import requests
import re

URL = 'http://127.0.0.1:5500/web_scraper/productos.html'

# Llamado al sitio web con requests
if __name__ == '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text

        # CREANDO COPIA HTML LOCAL DEL SITIO
        with open('scraper.html', 'w+', encoding='utf-8') as file:
            file.write(content)

        # PRIMERA FORMA DE OBTENER NOMBRES DE FRUTA.

        # regexa = '<td class="titulo">'
        # regexb = '</td>'

        # for line in content.split('\n'):

        #     if regexa in line:

        #         start = line.find(regexa) + len(regexa)
        #         end = line.find(regexb)

        #         title = line[start:end]
                
        #         print(title)

        # SEGUNDA FORMA DE OBTENER DATOS
        
    # TRABAJANDO CON EL ARCHIVO LOCAL
    with open('scraper.html', 'r', encoding='utf-8') as file:
        content = file.read()

        regex = '<td class="titulo">(.+?)</td>'

        line = re.findall(regex, content) # Listado de coicidencias.

        for title in line:
            print(title)




