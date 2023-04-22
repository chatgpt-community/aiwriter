import requests
import json


def get_links(url):
    response = requests.get(url)
    res_data = json.loads(response.text)
    original_data = []
    if res_data and res_data['data'] and res_data['data']['listingsPreview']:
        for item in res_data['data']['listingsPreview']:
            if not item['detailPageDisabled']:
                original_data.append(item['slug'])

    print('Valid response object count: ' + str(len(original_data)))

    articles_modified = []
    for article in original_data:
        articles_modified.append('https://gpt3demo.com/apps/' + article)

    return articles_modified
