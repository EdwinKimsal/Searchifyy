# Import(s)
import requests
from bs4 import BeautifulSoup

# Function to get links from sitemap
def sitemap_links(input, output):
    # Iterate through each sitemap in txt file
    with open(input, "r") as sitemaps:
        for sitemap in sitemaps:
            # Empty list to add links from sitemap
            urls_from_xml = []

            # Print sitemaps
            print(sitemap.strip("\n"))

            # Requesting the site
            site = requests.get(sitemap)
            print(site)

            # Getting content
            content = BeautifulSoup(site.content, "xml")

            # Getting all loc
            loc_tags = content.find_all('loc')

            # Getting link in from each loc
            for loc in loc_tags:
                urls_from_xml.append(loc.get_text())

            # Append to output file
            with open(output, "a") as text_file:
                for link in urls_from_xml:
                    text_file.write(f"{link}\n")