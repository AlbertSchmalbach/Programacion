from bs4 import BeautifulSoup

if __name__ == '__main__':
    
    with open('scraper.html', 'r', encoding='utf-8') as file:
        content = file.read()

        # Obtener maquetado del sitio web
        soup = BeautifulSoup(content, 'html.parser')

        # Imprimir contenido del head
        # print(soup.head)
        # print(type(soup.head))

        # title = soup.find('title')

        # Contenido con etq
        # print(title)
        # Nombre etq
        # print(title.name)
        # Contenido
        # print(title.text) # Recomendado
        # Otra forma de obtener contenido de etq
        # print(title.get_text())

        # elements = soup.find_all('td')
        # elements = soup.find_all('td', {'class': ['titulo', 'precio']})
        

        # for element in range(len(elements)):
        #     if element % 2 == 0:
        #         print(elements[element].text, elements[element+1].text)

        # elements = soup.find_all('tr')

        # print(elements)

        # for element in elements:
        #     td_titulo = element.find('td', {'class':'titulo'})
        #     td_precio = element.find('td', {'class':'precio'})

        #     if td_titulo == None or td_precio == None:
        #         continue
        #     print(td_titulo.text, td_precio.text)

        # OBTENCION DE DATOS MEDIANTE CLASES CSS

        # 1 forma
        # for element in soup.find_all(attrs={'class':'precio'}):
        #     print(element.text)

        # 2 forma (Recomendado)
        # for element in soup.find_all(class_='precio'):
        #     print(element.text)

        # OBTENCION DE DATOS MEDIANTE NODOS HIJOS
        # tr = soup.find('tr', {'class':'filas'})
        # print(tr.contents) #lista

        # fruta = tr.contents[1]
        # precio = tr.contents[3]

        # print(fruta.text, precio.text)

        # for child in tr.children:
        #     print(child)

        # NODOS HERMANOS

        # td_titulo = soup.find('td', {'class', 'titulo'})
        # td_titulo = soup.find('td', string='Manzana') 
        # print(td_titulo.next_sibling.next_sibling)

        # for element in td_titulo.next_siblings:
        #     print(element)


        # NODOS PADRES
        td_precio = soup.find('td', class_='precio')
        # print(td_precio.parent.parent.parent.name)

        for parent in td_precio.parents:
            print(parent.name)
        

        