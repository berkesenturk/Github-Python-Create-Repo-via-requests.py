# themoviedb.org => film ve dizi arşivi
# themoviedb' nin sunduğu apiyi uygulamanızda kullanınız.
# Anahtar kelimeye göre arama
# En popüler film listesi
# Vizyondaki film listesi



#mesela gui üzerinden film gösterimi yapabilrsin

import requests
import json
class theMovieDb:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org/3'
        self.api_key = '7d9f4b6a83c6b4cd3822ec88291098dc'

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    def getSearchResults(self,keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()
    def getNowPlaying(self, region):
        response = requests.get(f"{self.api_url}/movie/now_playing?api_key={self.api_key}&language=en-US&page=1&region={region}")
        return response.json()

movieApi = theMovieDb()

while True:
    secim = input("1- Popular Movies\n2- Search Movies\n3 - On Theater\n4 - Exit\nSeçim: ")

    if secim == "4":
        break
    else: 
        if secim =="1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])
        if secim =="2":
            keyword = input("keyword: ")
            movies = movieApi.getSearchResults(keyword)
            for movie in movies["results"]:
                print(movie['name'])
        if secim =="3":

            region = input("region (ISO 3166-1 alpha-2): ")
            movies = movieApi.getNowPlaying(region)
            for movie in movies["results"]:
                print(movie["original_title"])













