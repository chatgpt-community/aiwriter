from tools.ContentFormatTools import parse_json_to_html_code, retrieve_data_from_json_list
from tools.FileTools import save_file, read_file
from sender.wechat.WechatSender import WechatSender


def wx_transform(root_path, json_file_name, json_source_content, ad_path):
    wechat_file_dir = root_path + '/wechat_source_results/'
    title = retrieve_data_from_json_list(json_source_content, 'h1')
    subtitle = retrieve_data_from_json_list(json_source_content, 'h2')
    source_link = retrieve_data_from_json_list(json_source_content, 'link')
    html_content = parse_json_to_html_code(json_source_content, ['section'])
    ad_json = read_file(ad_path, True)
    html_content += ad_json['content']
    wechat_message = {'title': '与ChatGPT一起打造更智能的产品之 ' + title['text'],
                      'subTitle': subtitle['text'] if subtitle and subtitle['text'].strip() else title['text'],
                      'content': html_content,
                      'sourceLink': source_link['text']}
    save_file(wechat_file_dir, json_file_name, wechat_message, True)
    return wechat_message
