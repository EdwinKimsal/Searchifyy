# imports
import requests
from bs4 import BeautifulSoup

# url of sitemap
link = 'https://terrytao.wordpress.com/sitemap.xml'

# requesting the site
site = requests.get(link)

# getting content
content = BeautifulSoup(site.content, "xml")

# empty array to add links from sitemap
urls_from_xml = []

# getting all loc
loc_tags = content.find_all('loc')

# getting link in from each loc
for loc in loc_tags:
    urls_from_xml.append(loc.get_text()) 

# File
text_file = open("sitemap.js", "w", errors="ignore")
text_file.write("var urlArray = " + str(urls_from_xml) + ";")
text_file.close()