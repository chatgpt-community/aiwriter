import requests
import json
from tools.FileTools import save_file


def get_links(url, current_location, root_path):
    response = requests.get(url)
    res_data = json.loads(response.text)
    original_data = []
    if res_data and res_data['data'] and res_data['data']['listingsPreview']:
        print('get links value successfully!')
        modify_location_file(current_location, len(res_data['data']['listingsPreview']), root_path)
        for item in res_data['data']['listingsPreview']:
            if not item['detailPageDisabled']:
                original_data.append(item['slug'])

    print('Valid response object count: ' + str(len(original_data)))

    articles_modified = []
    for article in original_data:
        articles_modified.append('https://gpt3demo.com/apps/' + article)

    return articles_modified


def modify_location_file(current_location, links_len, root_path):
    current_offset = current_location['gpt_demo3_offset'] + links_len
    location_value = {
        'gpt_demo3_offset': current_offset,
        'gpt_demo3_limit': current_location['gpt_demo3_limit'],
        'gpt_demo3_end': True if links_len < current_location['gpt_demo3_limit'] else False
    }
    save_file(root_path + '/resources/', 'currentLocation.json', location_value, True)
