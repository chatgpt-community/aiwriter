from crawler.Gpt3DemoArticleLinksSpider import get_links
from crawler.Gpt3DemoArticleSpider import generate_md_file
from parser.MDParser import gen_md_file
from wechat.WechatSender import WechatSender

import os
import json


def run():
    links = get_links()
    root_path = os.path.dirname(os.path.abspath(__file__))
    for link in links:
        file_name = generate_md_file(link, root_path + '/json_results/')
        gen_md_file(file_name, root_path + '/resources/advertising.md', root_path + '/md_results/')
        break


if __name__ == "__main__":
    run()
    WechatSender().send({'title': 'Test Article2', 'subTitle': 'Test Subtitle2', 'content': 'Test Content2'})
    # event = ''
    # with open('md_results/result-teamsmart-ai.md', 'r') as file:
    #     event = json.load(file)
