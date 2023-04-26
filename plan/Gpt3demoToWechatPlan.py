import os
import time

from plan import Gpt3demoToJsonSourceSubPlan
from sender.wechat.WechatSender import WechatSender
from tools.FileTools import read_file
from transfer.json.WxOfficialAccountTransfer import wx_transform


def execute(root_path):
    Gpt3demoToJsonSourceSubPlan.execute(root_path)

    source_dir = root_path + '/.results/json_source_results/'
    results_source_dir = root_path + '/.results'
    ad_path_json = root_path + '/resources/advertising.json'
    sender = WechatSender()
    for root, dirs, files in os.walk(source_dir):
        handle_files(source_dir, files, ad_path_json, results_source_dir, sender)


def handle_files(json_source_dif, files, ad_path_json, results_source_dir, sender):
    for file in files:
        handle_single_file(json_source_dif, file, ad_path_json, results_source_dir, sender)
        time.sleep(0.5)


def handle_single_file(json_source_path, name, ad_path_json, results_source_dir, sender):
    json_source_content = read_file(json_source_path + name, True)
    message = wx_transform(results_source_dir, name, json_source_content, ad_path_json)
    sender.send(message)
