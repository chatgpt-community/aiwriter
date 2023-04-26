from tools.ContentFormatTools import parse_json_data_to_md, retrieve_data_from_json_list
from tools.FileTools import read_file, save_file
from tools.StringTools import replace


def planet_transform(results_source_dir, name, json_source_content, ad_path_md):
    md_file_dir = results_source_dir + '/md_results/'
    md_file_name = replace(name, '.json', '.xinqiu')
    source_link = retrieve_data_from_json_list(json_source_content, 'link')
    md_content = parse_json_data_to_md(json_source_content, ['section', 'h1', 'h2'])
    md_content += "\n" + "原文链接: " + source_link['text']
    md_content += "\n" + read_file(ad_path_md, False)
    save_file(md_file_dir, md_file_name, md_content, False)
    return md_content
