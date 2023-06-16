# imports
from bs4 import BeautifulSoup
import requests
import random
import time # time.sleep(x)

# random, range .5s to 1s
x = random.randint(5, 10) * .1

# original url
url = 'https://books.toscrape.com/'

# link
link = 'a[href]'

# urlArray/titleArray/htmlArray
urlArray = []
titleArray = []
htmlArray = []

# initial variables
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

# finding all urls
for a in soup.select(link):
    if 'https://books.toscrape.com/' + a.get("href") not in urlArray and "https://" not in str(a):
        urlArray.append('https://books.toscrape.com/' + a.get("href"))

        # new variables
        url = "https://books.toscrape.com/" + a.get("href")
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")

        # getting titles
        for t in soup.find("title"):
            titleArray.append(t.get_text())

        # appending info to htmlArray
        htmlArray.append(str(soup))
    
# File
text_file = open("sitemap.js", "w", errors="ignore")
text_file.write("var urlArray = " + str(urlArray) + ";" + "var titleArray = " + str(titleArray) + ";" + "var htmlArray = " + str(htmlArray).lower())
text_file.close()