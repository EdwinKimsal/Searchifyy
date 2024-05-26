# Searchifyy
<img align="center" src="https://github.com/EdwinKimsal/Searchifyy/assets/107333344/00fc0e22-425c-4989-9ea8-fda67e26d8be">

## Folders & Files
<ul>
  <li>Bad Data</li>
  <ul>
    <li>Includes data files that are currently unuseable</li>
  </ul>

  <br>

  <li>Data</li>
  <ul>
    <li>Includes data files that are currently useable</li>
    <li>Includes the combine.py file that combines the numerous data files into one singular file.</li>
  </ul>

  <br>

  <li>Frontend</li>
  <ul>
    <li>Includes the files that are used to create the interface that the user interacts interacts with. The code.js file includes the ranking code.</li>
  </ul>

  <br>
  
  <li>Python Backend</li>
  <ul>
    <li>Includes the crawl.py file that is used to crawl the web based off of a singular or multiple seed websites using numerous constraints.</li>
    <li>Includes the sitemap.py file that is used to obtain data from a sitemap link and has few constraints.</li>
  </ul>
</ul>

## Summary
This project is a work in progress, but it is a simple search engine that can handle multi-worded queries. It searches through 3+ million pages that were either crawled or taken from a sitemap with a Python script. Multiple websites were used. This search engine gives each page a score which is used to rank the pages based on the query. The higher the score the higher the page will rank. The score is determined by adding the scores of each word. The score of each word is the frequency of the word in the URL divided by the number of pages that contain the word. This is heavily based on [this video by Computerphile](https://www.youtube.com/watch?v=vrjAIBgxm_w).
