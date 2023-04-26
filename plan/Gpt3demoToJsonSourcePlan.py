import time

from crawler.Gpt3DemoArticleSpider import crawl
from crawler.Gpt3DemoArticleLinksSpider import get_links
from tools.FileTools import save_file, read_file, delete_dir


def execute(root_path):
    results_path = root_path + '/results/'
    delete_dir(results_path)
    links = retrieve_part_links(results_path, root_path)

    for link in links:
        print('Current Link: ' + link)
        handle_single_link(results_path, link)
        print('Link: ' + link + ' Successfully!')
        time.sleep(0.5)


def retrieve_part_links(results_path, root_path):
    location_file_name = root_path + '/resources/currentLocation.json'
    current_location = read_file(location_file_name, True)
    url = 'https://apideck-app-graphql.graphcdn.app/?operationName=listingsPreviewQuery&variables={"offset":' + \
          str(current_location['gpt_demo3_offset']) + ',"limit":' + str(current_location['gpt_demo3_limit']) + \
          ',"ecosystemId":"ckhg56iu1mkpc0b66vj7fsj3o"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"92e140fa09030567de6c07cf641b0c2b381817f5d2311df4c0faeff27a04700d"}}'
    links = get_links(url, current_location, root_path)
    save_file(results_path + '/links_results', 'link.json', links, True)
    return links


def handle_single_link(root_path, link):
    json_file_dir = root_path + '/json_source_results/'
    crawl(link, json_file_dir)
