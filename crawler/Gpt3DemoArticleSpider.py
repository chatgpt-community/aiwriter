from lxml import html
from tools.ContentFormatTools import parse_html_to_json_dic
from tools.FileTools import save_file
from tools.StringTools import find_last_word_in_url
import requests


def crawl(url, save_path):
    response = requests.get(url)
    tree = html.fromstring(response.content)
    listing_body_elements = tree.xpath('//*[contains(@class, "listing-body")]/*')

    section_count = 0
    selected_elements = []
    for element in listing_body_elements:
        if element.tag in ['h1', 'h2', 'section']:
            if element.tag == 'section' and section_count > 0:
                continue
            selected_elements.append(element)
            if element.tag == 'section':
                section_count += 1

    json_data = []
    for element in selected_elements:
        json_data.append(parse_html_to_json_dic(html.tostring(element).decode('utf-8'), True))

    json_data.append({'tag': 'link', 'text': url})
    json_file_name = find_last_word_in_url(url) + '.json'
    save_file(save_path, json_file_name, json_data, True)
    return json_file_name
