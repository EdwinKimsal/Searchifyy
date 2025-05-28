# Searchifyy
<img align="center" src="https://github.com/EdwinKimsal/Searchifyy/assets/107333344/00fc0e22-425c-4989-9ea8-fda67e26d8be">

## Overview
Searchifyy is a small search engine that was made for developers to be used as a learning tool. If developers can learn how a search engine works, then these developers can create better queries that yield better results in daily use. This search engine was created from scratch through the use of Python, HTML, CSS, and JavaScript. Python was used for crawling and indexing, while HTML, CSS, and JavaScript were used for ranking.

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

## Index
This is the collection of the data that is used by Searchifyy to provide users results based off of his or her query. This data includes the URL's of over 150,000 websites under numerous domains, which were purposely selected to answer the needs of computer science students. Some of these domains include Wikipedia, GeeksForGeeks, The Odin Project, and Calculator Soup.

## Scoring Algorithm
The image below demonstrates how each site is given a score based on the user's query. A high score relates to high relevancy while a low score relates to low relevancy. All scores given are zero or greater, where a score of zero relates to zero relevancy.
<img align="center" src="https://github.com/EdwinKimsal/Searchifyy/assets/107333344/fd7d9b77-bef6-46ad-aa61-a9b6d8153561">

## Sorting Algorithm
Essentially, each site is given a score as stated in the section _Scoring Algorithm_. After each site gets a score, all zero-scores are removed, and a sorting algorithm ranks the websites from the greatest score (highest rank) to the lowest score (lowest rank).

<ul>
    <li>Heap Sort</li>
    <ul>
      <li>Comparison Based</li>
      <li>Complete Binary Tree</li>
      <li>O(n * log (n))</li>
    </ul>
</ul>

## Website
https://searchifyy.netlify.app/
