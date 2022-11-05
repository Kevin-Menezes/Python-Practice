from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Top Rated Movies"
sheet.append(["Movie rank","Movie name","Year of release","Movie ratings"])


try:
    source = requests.get("https://www.imdb.com/chart/top/")
    source.raise_for_status() # This is used to give an error in the console if the url is invalid

    soup = BeautifulSoup(source.text,"html.parser")

    movie_details = soup.find("tbody",class_="lister-list").find_all("tr") # List that consists of many tr
    
    for movie in movie_details:
        movie_rank = movie.find("td",class_="titleColumn").get_text(strip=True).split(".")[0]
        movie_name = movie.find("td",class_="titleColumn").a.text
        movie_year = movie.find("td",class_="titleColumn").span.text.strip("()")
        movie_rating = movie.find("td",class_="ratingColumn imdbRating").strong.text.strip()

        print(movie_rank,movie_name,movie_year,movie_rating)
        sheet.append([movie_rank,movie_name,movie_year,movie_rating])
        

except Exception as e:
    print(e)


excel.save("2)_IMDB//IMDB Movie Ratings.xlsx")