import requests
from bs4 import BeautifulSoup
import os
import re
import json


def generate_md_file(url, json_path):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    listing_body = soup.find('div', class_='listing-body')
    elements = []
    section_count = 0
    for element in listing_body:
        if element.name in ['h1', 'h2', 'section']:
            if section_count > 0 and element.name == 'section':
                continue
            if element.name == 'h1':
                elements.append({
                    "tag": "title",
                    "content": element.text
                })
            if element.name == 'h2':
                elements.append({
                    "tag": "subtitle",
                    "content": element.text
                })
            if element.name == 'section':
                section_count += 1
                cleand_html_code = re.sub(r'\s(class|id|name|style|href)="[^"]*"', '', element.prettify())
                compressed_line = ''.join(cleand_html_code.splitlines())
                elements.append({
                    "tag": "main",
                    "content": compressed_line
                })
    elements.append({
        "tag": "link",
        "content": url
    })
    if not os.path.exists(json_path):
        os.makedirs(json_path)

    filename = 'result-' + url.split("/")[-1] + '.json'
    file_path = os.path.join(json_path, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(elements, ensure_ascii=False, indent=4))
    return file_path
