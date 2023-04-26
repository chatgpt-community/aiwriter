import os
import time

from plan import Gpt3demoToJsonSourceSubPlan
from sender.xinqiu.XinQiu import XinQiu
from tools.FileTools import read_file
from transfer.xinqiu import HtmlTransfer
from transfer.xinqiu.MarkdownTransfer import planet_transform


def execute(root_path):
    # Gpt3demoToJsonSourceSubPlan.execute(root_path)
    source_dir = root_path + '/.results/json_source_results/'
    results_source_dir = root_path + '/.results'
    for root, dirs, files in os.walk(source_dir):
        handle_files(source_dir, files, results_source_dir)


def handle_files(json_source_dif, files, results_source_dir):
    for file in files:
        try:
            handle_single_file(json_source_dif, file, results_source_dir)
        except Exception as e:
            print(e)


def handle_single_file(json_source_path, name, results_source_dir):
    json_source_content = read_file(json_source_path + name, True)
    content = HtmlTransfer.transfer(results_source_dir, name, json_source_content)
    event = {'content': content}
    XinQiu().send(event)

