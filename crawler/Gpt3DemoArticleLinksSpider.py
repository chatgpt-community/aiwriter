import requests
from bs4 import BeautifulSoup


def get_links():
    url = "https://gpt3demo.com"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    page_content_container = soup.find('div', class_='page-content-container')
    listings = page_content_container.find('div', class_='listings')
    grid_roots = listings.find_all('div', class_='MuiGrid-root')

    articles = []
    for grid_root in grid_roots:
        for a_tag in grid_root.find_all('a'):
            href = a_tag.get('href')
            articles.append(href)

    articles_modified = []
    for article in articles:
        if article.startswith('/apps'):
            articles_modified.append('https://gpt3demo.com' + article)
        elif article not in ['/partner/request', '#']:
            articles_modified.append(article)

    return articles_modified
