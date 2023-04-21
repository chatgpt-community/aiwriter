from tools.ContentFormatTools import parse_json_data_to_md
from tools.FileTools import read_file, save_file
from tools.StringTools import replace


def planet_transform(json_content, json_file_name, link, root_path, ad_path):
    md_file_dir = root_path + '/md_results/'
    md_file_name = replace(json_file_name, '.json', '.md')
    md_content = parse_json_data_to_md(json_content, ['section', 'h1', 'h2'])
    md_content += "\n" + "原文链接: " + link
    md_content += "\n" + read_file(ad_path, False)
    save_file(md_file_dir, md_file_name, md_content, False)
