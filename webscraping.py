import requests
from bs4 import BeautifulSoup


# Función para realizar web scraping en la página de "Top 250" de IMDb
def obtener_top_peliculas(num_peliculas=10):
    url = "https://www.imdb.com/chart/top/"

    # Realizar una solicitud HTTP GET para obtener el contenido de la página web
    respuesta = requests.get(url)
    contenido_web = respuesta.content

    # Utilizar BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(contenido_web, "html.parser")

    # Buscar todos los elementos de la tabla de películas
    tabla_peliculas = soup.find("tbody", class_="lister-list")
    filas_peliculas = tabla_peliculas.find_all("tr")[:num_peliculas]

    # Extraer la información de cada película y agregarla a una lista
    lista_peliculas = []
    for fila in filas_peliculas:
        titulo = fila.find("td", class_="titleColumn").a.text
        año = fila.find("span", class_="secondaryInfo").text.strip("()")
        rating = fila.find("td", class_="ratingColumn imdbRating").strong.text

        pelicula = {
            "titulo": titulo,
            "año": año,
            "rating": rating
        }
        lista_peliculas.append(pelicula)

    # Imprimir la lista de películas
    for index, pelicula in enumerate(lista_peliculas, start=1):
        print(f"{index}. {pelicula['titulo']} ({pelicula['año']}) - Rating: {pelicula['rating']}")


# Llamar a la función para mostrar las películas
if __name__ == "__main__":
    obtener_top_peliculas()
    