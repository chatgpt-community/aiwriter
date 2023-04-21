from crawler.Gpt3DemoArticleLinksSpider import get_links
from crawler.Gpt3DemoArticleSpider import generate_md_file
from sender.wechat.WechatSender import WechatSender
from parser.MDParser import gen_md_file
import os


def execute():
    # add logic here...
    # links = get_links()
    # root_path = os.path.dirname(os.path.abspath(__file__))
    # for link in links:
    #     file_name = generate_md_file(link, root_path + '/json_results/')
    #     gen_md_file(file_name, root_path + '/resources/advertising.md', root_path + '/md_results/')
    #     break
    sender = WechatSender()
    sender.send({'title': 'Test Article2', 'subTitle': 'Test Subtitle2', 'content': 'Test Content2'})