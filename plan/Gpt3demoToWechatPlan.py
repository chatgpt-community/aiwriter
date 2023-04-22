import time

from crawler.Gpt3DemoArticleSpider import crawl
from crawler.Gpt3DemoArticleLinksSpider import get_links
from tools.FileTools import read_file, save_file
from transfer.md.PlanetArticleTransfer import planet_transform
from transfer.json.WxOfficialAccountTransfer import wx_transform


def execute(root_path):
    ad_path_md = root_path + '/resources/advertising.md'
    ad_path_json = root_path + '/resources/advertising.json'

    results_path = root_path + '/results'
    links = retrieve_all_links(results_path)

    c = 0
    for link in links:
        if c == 10:
            return
        print('Current Link: ' + link)
        handle_single_link(results_path, link, ad_path_json, ad_path_md)
        print('Link: ' + link + ' Successfully!')
        time.sleep(0.5)
        c += 1


def retrieve_all_links(root_path):
    url = 'https://apideck-app-graphql.graphcdn.app/?operationName=listingsPreviewQuery&variables={"offset":0,"limit":900,"ecosystemId":"ckhg56iu1mkpc0b66vj7fsj3o"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"92e140fa09030567de6c07cf641b0c2b381817f5d2311df4c0faeff27a04700d"}}'
    links = get_links(url)
    save_file(root_path + '/links_results', 'link.json', links, True)
    return links


def handle_single_link(root_path, link, ad_path_json, ad_path_md):
    json_file_dir = root_path + '/json_source_results/'
    json_file_name = crawl(link, json_file_dir)

    json_source_content = read_file(json_file_dir + json_file_name, True)
    planet_transform(json_source_content, json_file_name, link, root_path, ad_path_md)
    wx_transform(root_path, json_file_name, json_source_content, ad_path_json, link)
