import bs4
import requests;

#URL sin número de página (se espera este número).
URL = 'https://books.toscrape.com/catalogue/page-{}.html'

# Títulos que se agregarán a la lista de 4 o 5 estrellas.
titulos4o5Est = []

for i in range(1, 52):
    # Sopa de cada página
    URLPag = URL.format(i)
    res = requests.get(URLPag)
    sopa = bs4.BeautifulSoup(res.text, 'lxml')

    # Libros seleccionados
    libros = sopa.select('.product_pod')

    for libro in libros:
        # Validación de estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):
            #Almacenar título.
            titLib = libro.select('a')[1]['title']

            #Agregar el libro almacenado a la lista.
            titulos4o5Est.append(titLib)

#Visualizar libros.
for t in titulos4o5Est:
    print(t)