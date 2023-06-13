# imports
from bs4 import BeautifulSoup
import requests
import random
import time # time.sleep(x)

# random, range .5s to 1s
x = random.randint(5, 10) * .1

# original url
url = 'https://quotes.toscrape.com/'

# link
link = 'a[href]'

# urlArray/htmlArray
urlArray = []
htmlArray = []

# initial variables
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

# finding all urls
for a in soup.select(link):
    if 'https://quotes.toscrape.com' + a.get("href") not in urlArray and "https://" not in str(a):
        urlArray.append('https://quotes.toscrape.com' + a.get("href"))

        # new variables
        url = "https://quotes.toscrape.com" + a.get("href")
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")

        # appending info to htmlArray
        htmlArray.append(str(soup))

# File
text_file = open("sitemap.js", "w", errors="ignore")
text_file.write("var urlArray = " + str(urlArray) + ";" + "var htmlArray = " + str(htmlArray).lower())
text_file.close()