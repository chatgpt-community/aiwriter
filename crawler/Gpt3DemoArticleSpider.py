import requests
from bs4 import BeautifulSoup
import json
import sys

# Step 1: Get the html code from the website
url = sys.argv[1]
response = requests.get(url)
html = response.content

# Step 2: Filter the elements in the html code
soup = BeautifulSoup(html, 'html.parser')
listing_body = soup.find('div', class_='listing-body')
elements = []
sectionCount = 0
for element in listing_body:
    if element.name in ['h1', 'h2', 'section']:
        if sectionCount > 0 and element.name == 'section':
            continue
        if element.name == 'section':
            sectionCount += 1
        elements.append({
            'tag': element.name,
            'content': element.get_text(separator='\n').strip()
        })

# Step 3: Convert the filtered html elements into json format
json_data = json.dumps(elements, ensure_ascii=False, indent=4)

# Step 4: Save the converted json data to a file
with open('result-' + url.split("/")[-1]+'.json', 'w', encoding='utf-8') as f:
    f.write(json_data)
