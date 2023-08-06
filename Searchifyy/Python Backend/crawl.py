# imports
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import random
import time

# whiteList, que, pushQue
whiteList = 'https://www.tutorialrepublic.com/'
que = [whiteList]
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

            # sleep for random time
            x = random.randint(1, 3)
            time.sleep(x)
            print(x)

            # getting links
            for a in soup.select(link):
                linkGet = a.get("href")

                # joining url
                url = urljoin(site, linkGet)

                # checking if the site is new
                if url not in urlArray and url not in que and url not in pushQue and url.startswith(whiteList):
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
text_file = open("crawl.js", "w", errors="ignore")
text_file.write("var urlArray = " + str(urlArray) + ";")
text_file.close()