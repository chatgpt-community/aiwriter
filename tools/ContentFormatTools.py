from lxml import html
from tools.StringTools import remove_html_comment
from tools.TranslateTools import translate


def parse_json_data_to_md(json_content, target_tags):
    md = ""
    for element in json_content:
        tag = element.get("tag")
        if tag in target_tags:
            md += parse_json_node_to_md(element)
    return md


def parse_json_node_to_md(json_data):
    md = ''
    if json_data['tag'] == 'p':
        md += json_data['text'] + '\n\n'
    elif json_data['tag'] == 'h1':
        md += '# ' + json_data['text'] + '\n\n'
    elif json_data['tag'] == 'h2':
        md += '## ' + json_data['text'] + '\n\n'
    elif json_data['tag'] == 'h3':
        md += '### ' + json_data['text'] + '\n\n'
    elif json_data['tag'] == 'ul':
        for child in json_data['children']:
            md += '- ' + child['text'] + '\n'
        md += '\n'
    elif json_data['tag'] == 'ol':
        for i, child in enumerate(json_data['children']):
            md += str(i + 1) + '. ' + child['text'] + '\n'
        md += '\n'
    else:
        md += json_data['text'] + '\n\n'
    if 'children' in json_data:
        for child in json_data['children']:
            md += parse_json_node_to_md(child)
    return md


def parse_json_to_html_code(data, target_tags):
    html_code = ""
    for item in data:
        if not target_tags or item["tag"] in target_tags:
            tag = item["tag"]
            text = item["text"]
            children = parse_json_to_html_code(item["children"], []) if item["children"] else ""
            html_code += f"<{tag}>{text}{children}</{tag}><br/>"
    return html_code


def parse_html_to_json_dic(html_code, need_translate):
    tree = html.fromstring(remove_html_comment(html_code))
    return parse_element(tree, need_translate)


def parse_element(element, need_translate):
    text_content = element.text.strip() if element.text else ''
    text_content = translate(text_content) if need_translate and text_content and element.tag != 'h1' else text_content
    json_dict = {'tag': element.tag, 'text': text_content, 'children': []}
    for child in element:
        json_dict['children'].append(parse_element(child, need_translate))
    return json_dict
