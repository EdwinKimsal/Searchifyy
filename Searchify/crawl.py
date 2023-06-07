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

# sitemap
sitemap = []

# applying request and soup
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')

# appending urls
for a in soup.select(link):
    if a not in sitemap and 'https://' not in str(a):
        sitemap.append(a.get('href'))

# printing sitemap
print(sitemap)

# File
text_file = open("sitemap.js", "w")
text_file.write('var sitemap = ' + str(sitemap) +';')
text_file.close()