# imports
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import random
import time

# seed, que, pushQue
seed = 'https://www.w3schools.com/'
que = [seed]
pushQue = []

# depth
depth = 2

# link
link = 'a[href]'

# urlArray
urlArray = []

# finding all urls per depth
def urlSearch():
    for site in que:
        # checking if any sites are in que
        if len(que) > 0:
            # setting up variables
            request = requests.get(site)
            soup = BeautifulSoup(request.text, "html.parser")

            # getting links
            for a in soup.select(link):
                linkGet = a.get("href")

                # joining url
                url = urljoin(site, linkGet)

                # sleep for random time
                # x = random.randint(1, 3)
                # time.sleep(x)
                # print(x)

                # checking if the site is new
                if url not in urlArray and url not in que and url not in pushQue and url.startswith(seed):
                    # getting urls
                    urlArray.append(url)
                    pushQue.append(url)
                    print(url)

            # getting rid of site in que
            que.remove(site)

# calling urlSearch()
for x in range(depth):
    urlSearch()
    que = pushQue
    pushQue = []
    
# File
text_file = open("sitemap.js", "w", errors="ignore")
text_file.write("var urlArray = " + str(urlArray) + ";")
text_file.close()