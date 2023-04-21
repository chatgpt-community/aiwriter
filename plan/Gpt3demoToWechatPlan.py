import time

from crawler.Gpt3DemoArticleSpider import crawl
from crawler.Gpt3DemoArticleLinksSpider import get_links
from tools.FileTools import read_file, save_file
from transfer.md.PlanetArticleTransfer import planet_transform
from transfer.json.WxOfficialAccountTransfer import wx_transform


def execute(root_path):
    ad_path_md = root_path + '/resources/advertising.md'
    ad_path_json = root_path + '/resources/advertising.json'
    root_path += "/results"
    try:
        links = retrieve_links(root_path)
    except Exception as e:
        print('Error: retrieve links error!', e)
        return

    c = 0
    for link in links:
        try:
            if c == 2:
                return
            handle_single_link(root_path, link, ad_path_json, ad_path_md)
            print("Link: " + link + " Successfully!")
            time.sleep(0.5)
            c += 1
        except Exception as e:
            print('Error: Handle article error!, Link: ' + link, e)
            continue


def retrieve_links(root_path):
    links = get_links()
    save_file(root_path + '/links_results', 'link.json', links, True)
    return links


def handle_single_link(root_path, link, ad_path_json, ad_path_md):
    json_file_dir = root_path + '/json_source_results/'
    json_file_name = crawl(link, json_file_dir)

    json_source_content = read_file(json_file_dir + json_file_name, True)
    planet_transform(json_source_content, json_file_name, link, root_path, ad_path_md)
    wx_transform(root_path, json_file_name, json_source_content, ad_path_json, link)
