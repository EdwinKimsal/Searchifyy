# Import(s)
import time
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to get links from sitemap
def sitemap_links(input, output):
    # Empty list to add links from sitemap
    urls_from_xml = []

    # Create a blacklist
    blacklist = ["?", "=try", "/tryit", "/show", "_quiz", "_exercise", "/exercise", ".xml", ".png", ".PNG", ".jpg", ".jpeg", ".webp", ".gif", ".GIF"]

    # Iterate through each sitemap in txt file
    with open(input, "r") as sitemaps:
        for sitemap in sitemaps:
            # Strip from sitemap
            sitemap = sitemap.strip("\n")
            sitemap = sitemap.strip("\r")

            # Requesting the site
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2810.1 Safari/537.36'}
            site = requests.get(sitemap, auth=('user', 'pass'), headers=headers)

            # Print link and response
            print(sitemap)
            print(f"{site}\n")

            # Getting content
            content = BeautifulSoup(site.content, "xml")

            # Getting all loc
            loc_tags = content.find_all('loc')

            # Getting link in from each loc if valid
            for loc in loc_tags:
                if all(word not in loc.get_text() for word in blacklist):
                    urls_from_xml.append(loc.get_text())

    # Write output by calling function
    write_output(urls_from_xml, output)


# Function to get links by mapping
def map_links(input, output, depth, max_sleep):
    # Set a blacklist
    blacklist = ["wiki/Wikipedia", "Wikimedia", "Category", "Articles", "Template", "Portal", "Special", "Help", "File", "Talk", "#", "(", ")", "%", "?", "=try", "/tryit", "/show", "_quiz", "_exercise", "/exercise", ".xml", ".png", ".PNG", ".jpg", ".jpeg", ".webp", ".gif", ".GIF"]

    # Set variable for type looking for
    type_to_find = "a[href]"

    # Create four empty lists to dump links and track main urls
    links = []
    urls = []
    que = ["https://en.wikipedia.org/wiki/Computer_science"]
    found_links = []

    # Iterate through each file in maps and append to urls and que
    with open(input, "r") as maps:
        for map in maps:
            urls.append(map)

    # Iterate through each URL in maps file
    for site in urls:
        # Iterate through maps for designated depth
        for layer in range(depth):
            # Iterate through each link at this layer
            for link in que:
                # Make a request for link and get text
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2810.1 Safari/537.36'}
                response = requests.get(link, auth=('user', 'pass'), headers=headers)
                soup = BeautifulSoup(response.text, "html.parser")

                # Print link and response
                print(link)
                print(response)

                # Find all redirects in link
                for a in soup.select(type_to_find):
                    redirect = a.get("href")
                    url = urljoin(link, redirect) # Join url

                    # Add url to found links
                    found_links.append(url)

                # Sleep for the random allotted time
                if max_sleep > 0:
                    sleep_time = random.random() * max_sleep
                    print(f"{sleep_time}\n")
                    time.sleep(sleep_time)

            # Reset que
            links += que # Add links in que to all links
            que = [] # Empty que

            # Add newly found links to que and reset found links
            for link in found_links:
                if link not in links and link not in que and link.startswith(site):
                    if all(word not in link for word in blacklist):
                        que.append(link)
            found_links = [] # Empty found links

            # Add links stuck in que to all links
            links += que

    # Write output by calling function
    write_output(links, output)


# Function to write in output file
def write_output(list, output):
    # Append to output file
    with open(output, "a") as text_file:
        for link in list:
            text_file.write(f"{link}\n")


# Function to combine two text files
def combine(final_file, from_file):
    # Set a blank list to store links
    links = []

    # Open from file and extract all links
    with open(from_file, "r") as f:
        for link in f:
            links.append(link)

    # Open final file and add all links that are not already there
    with open(final_file, "r+") as f:
        lines = [line.strip("\n") for line in f.readlines()]
        print(lines)
        for link in links:
            if link not in lines:
                f.writelines(link)