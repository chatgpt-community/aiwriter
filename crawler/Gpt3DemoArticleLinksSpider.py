import requests
from bs4 import BeautifulSoup
import json

# Step 1: Send a GET request to the website and get the HTML content
url = "https://gpt3demo.com"
response = requests.get(url)

# Step 2: Parse the HTML content and find the elements
soup = BeautifulSoup(response.content, 'html.parser')
page_content_container = soup.find('div', class_='page-content-container')
listings = page_content_container.find('div', class_='listings')
grid_roots = listings.find_all('div', class_='MuiGrid-root')

# Step 3: Traverse the elements and get the href attribute of all 'a' tags
articles = []
for grid_root in grid_roots:
    for a_tag in grid_root.find_all('a'):
        href = a_tag.get('href')
        articles.append(href)

# Step 4: Traverse the list and modify the items as needed
articles_modified = []
for article in articles:
    if article.startswith('/apps'):
        articles_modified.append('https://gpt3demo.com' + article)
    elif article not in ['/partner/request', '#']:
        articles_modified.append(article)

# Step 5: Save the modified list to a JSON file
data = {"articles": articles_modified}
with open("articleList.json", "w") as file:
    json.dump(data, file)
