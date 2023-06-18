# Searchifyy
This project is a work in progress, but it is a simple search engine that can handle multi-worded queries. It searches through a few dozen pages that were crawled through https://books.toscrape.com. This search engine gives each page a score which is used to rank the pages based on the query. The higher the score the higher the page will rank. The score is determined by adding the scores of each word. The scores of each word is the freqiency of the word divided by the amount of pages that contain the word. This is heavily based on this video by Computerphile (https://www.youtube.com/watch?v=vrjAIBgxm_w).

Websites: https://searchifyy.netlify.app
