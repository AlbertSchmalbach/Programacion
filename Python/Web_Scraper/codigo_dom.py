from bs4 import BeautifulSoup

if __name__ == '__main__':

    with open('scraper.html', 'r', encoding='utf-8') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        # MODIFICAR NODOS
        # td_filas = soup.find('tr', {'class':'filas'})

        # print(td_filas.get('classe', 'No existe'))
        # td_filas['id'] = 'fila1'
        # td_filas['titulo'] = 'Nueva fila'

        # td_filas.td.string = 'Mora'
        # precio = td_filas.find('td', {'class': 'precio'})
        # precio.string = '$2000'
        # print(precio.string)

        # print(soup.prettify())

        # CREAR NODOS
        # td = soup.new_tag('td', class_='titulo')
        # td.string = 'Guayaba'
        # tr = soup.new_tag('tr', class_= 'fila')

        # tr.append('\n')
        # tr.append(td)
        # tr.append('\n')

        # soup.tbody.append(tr)
        # soup.tbody.insert(0, tr)

        # print(soup.prettify())

        # ELIMINAR NODOS
        td_filas = soup.find('tr', {'class':'filas'})

        # td_filas.contents = []

        td_filas.td.string = ''

        td = td_filas.td.extract()

        # print(td_filas)
        print(td)




