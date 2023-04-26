import os
from tools.FileTools import read_file
from transfer.md.PlanetArticleTransfer import planet_transform


def execute(root_path):
    source_dir = root_path + '/results/json_source_results/'
    results_source_dir = root_path + '/results'
    ad_path_json = root_path + '/resources/advertising.md'
    for root, dirs, files in os.walk(source_dir):
        handle_files(source_dir, files, ad_path_json, results_source_dir)


def handle_files(json_source_dif, files, ad_path_json, results_source_dir):
    for file in files:
        handle_single_file(json_source_dif, file, ad_path_json, results_source_dir)


def handle_single_file(json_source_path, name, ad_path_md, results_source_dir):
    json_source_content = read_file(json_source_path + name, True)
    planet_transform(results_source_dir, name, json_source_content, ad_path_md)

