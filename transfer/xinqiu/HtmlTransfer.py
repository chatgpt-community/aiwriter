from tools.ContentFormatTools import parse_json_to_html_code, retrieve_data_from_json_list
from tools.FileTools import save_file, read_file
from sender.wechat.WechatSender import WechatSender


def transfer(root_path, json_file_name, json_source_content):
    wechat_file_dir = root_path + '/wechat_source_results/'
    title = retrieve_data_from_json_list(json_source_content, 'h1')
    subtitle = retrieve_data_from_json_list(json_source_content, 'h2')
    source_link = retrieve_data_from_json_list(json_source_content, 'link')
    html_content = parse_json_to_html_code(json_source_content, ['section']) + "<br/> [原文链接]" + source_link["text"]
    with_title = "<h1># " + title["text"] + "</h1><br/><p></p><h2>" + subtitle["text"] if subtitle and subtitle["text"] \
        else "" + "</h2>" + html_content
    save_file(wechat_file_dir, json_file_name, with_title, True)
    content = with_title.replace("<div>", "").replace("<section>", "").replace("</div>", "").replace("</section>", "")
    return content
