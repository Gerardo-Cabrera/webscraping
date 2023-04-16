import json
import requests
from bs4 import BeautifulSoup


class IMDbScraper:
    def __init__(self, movies_num=10):
        self.movies_num = movies_num
        self.movies_list = []
        self.url = "https://www.imdb.com/chart/top/"

    # Function to perform web scraping on the IMDb "Top 250" page
    def get_top_movies(self):
        url = self.url
        movies_num = self.movies_num

        # Make an HTTP GET request to get the content of the web page
        response = requests.get(url)
        web_content = response.content

        # Use BeautifulSoup to parse HTML content
        soup = BeautifulSoup(web_content, "html.parser")

        # Find all the elements of the cinema table
        movies_table = soup.find("tbody", class_="lister-list")
        movies_rows = movies_table.find_all("tr")[:movies_num]

        # Extract information from each movie and add it to a list
        movies_list = self.movies_list

        for row in movies_rows:
            title = row.find("td", class_="titleColumn").a.text
            year = row.find("span", class_="secondaryInfo").text.strip("()")
            rating = row.find("td", class_="ratingColumn imdbRating").strong.text

            movie = {
                "title": title,
                "year": year,
                "rating": rating
            }
            self.movies_list.append(movie)

        # Print the list of movies
        for index, movie in enumerate(movies_list, start=1):
            print(f"{index}. {movie['title']} ({movie['year']}) - Rating: {movie['rating']}")

        # Return the list of movies
        return movies_list

    def save_txt(self):
        with open("movies.txt", "w", encoding="utf-8") as txt_file:
            for index, movie in enumerate(self.movies_list, start=1):
                txt_file.write(f"{index}. {movie['title']} ({movie['year']}) - Rating: {movie['rating']}\n")

    def save_json(self):
        with open("movies.json", "w", encoding="utf-8") as json_file:
            json.dump(self.movies_list, json_file, ensure_ascii=False, indent=4)


# Call the functions to display the list of movies and save this information in txt and json files
if __name__ == "__main__":
    scraper = IMDbScraper()
    scraper.get_top_movies()
    scraper.save_txt()
    scraper.save_json()
