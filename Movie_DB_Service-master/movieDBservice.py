import tmdbsimple as tmdb
import requests
import json

#Class for a movie object
class Movie:
  def __init__(self, title, overview, releaseDate):
    self.title = title
    self.overview = overview
    self.releaseDate = releaseDate

#Function to seach for a movie within a list
def Search(alist):
  print("----------------------------------")
  search_input = input("Please enter your search query: ")
  for items in alist:
    if search_input.lower() == items.title or search_input == items.overview:
      print("-----------------------------------")
      print("Title: " + items.title)
      print("Release Date: "+ items.releaseDate)
      print("Overview: " + items.overview)
      print("")
  
#Populates the now_playing list for search function
def populate_np_list():
  #Now playing list
  np_list = []
  r = requests.get("https://api.themoviedb.org/3/movie/now_playing?page=1&api_key=9d3c8941bb5a7d5abef3326b3cd2cab8")
  raw = r.json()
  pages = True
  i = 1
  for page in range(raw['total_pages']):
    r = requests.get("https://api.themoviedb.org/3/movie/now_playing?page="+str(i)+"&api_key=9d3c8941bb5a7d5abef3326b3cd2cab8")
    raw = r.json()
    for j in raw['results']:
      movi = Movie(j['title'].lower(), j['overview'].lower(), j['release_date'])
      np_list.append(movi)
    i += 1
  return np_list

#Populates the upcoming_list for search function
def populate_upcoming_list():
  #upcomingList
  upcoming_list = []
  r = requests.get("https://api.themoviedb.org/3/movie/upcoming?page=1&api_key=9d3c8941bb5a7d5abef3326b3cd2cab8")
  raw = r.json()
  pages = True
  i = 1
  for page in range(raw['total_pages']):
    r = requests.get("https://api.themoviedb.org/3/movie/upcoming?page="+str(i)+"&api_key=9d3c8941bb5a7d5abef3326b3cd2cab8")
    raw = r.json()
    for j in raw['results']:
      movi = Movie(j['title'].lower(), j['overview'].lower(), j['release_date'])
      upcoming_list.append(movi)
    i += 1
  return upcoming_list

#Populates the Top_Rated list for search function
def populate_tr_list():
  #Top_RatedList
  tr_list = []
  r = requests.get("https://api.themoviedb.org/3/movie/top_rated?page=1&api_key=9d3c8941bb5a7d5abef3326b3cd2cab8")
  raw = r.json()
  pages = True
  i = 1
  for page in range(raw['total_pages']):
    r = requests.get("https://api.themoviedb.org/3/movie/top_rated?page="+str(i)+"&api_key=9d3c8941bb5a7d5abef3326b3cd2cab8")
    raw = r.json()
    for j in raw['results']:
      movi = Movie(j['title'].lower(), j['overview'].lower(), j['release_date'])
      tr_list.append(movi)
    i += 1
  return tr_list


#------------------------Driver---------------------------------
y = 1
while y == 1:
  print("Welcome to our Movie Database!")
  print("What content would you like to view?")
  print(" 1. View Now Playing \n 2. View Upcoming Releases \n 3. View Top Rated \n 4. Search all Movies \n 0. EXIT")
  user_input = int(input("Enter your choice here: "))

  if user_input == 1:
    np_list = populate_np_list()
    for items in np_list:
      print("-----------------------")
      print(items.title)
      print(items.releaseDate)
    Search(np_list)
  elif user_input == 2:
    upcoming_list = populate_upcoming_list()
    for items in upcoming_list:
      print("-----------------------")
      print(items.title)
      print(items.releaseDate)
    Search(upcoming_list)
  elif user_input == 3:
    tr_list = populate_tr_list()
    for items in tr_list:
      print("-----------------------")
      print(items.title)
      print(items.releaseDate)
    Search(tr_list)
  elif user_input == 4:
      search = input("Enter query here: ")
      r = requests.get("https://api.themoviedb.org/3/search/movie?query=" + str(search) +"&api_key=9d3c8941bb5a7d5abef3326b3cd2cab8")
      raw = r.json()
      pages = True
      i = 1
      for page in range(raw['total_pages']):
        r = requests.get("https://api.themoviedb.org/3/search/movie?query=" + str(search) +"&page=" + str(i) + "api_key=9d3c8941bb5a7d5abef3326b3cd2cab8")
        raw = r.json()
      for j in raw['results']:
        print("---------------------")
        print(j['title'])
        print(j['release_date'])
      i += 1
  elif user_input == 0:
    print("Thank you for using our Database! \nGood-Bye!")
    y = 0
  else:
    print("Please enter a choice")
    y = 1
