import json
import os
import html2text
import re

from .TranslateTool import translate


def gen_md_file(file_path, ad_path, md_path):
    if not os.path.exists(md_path):
        os.makedirs(md_path)
    content = read_json_file(file_path)
    ad_content = read_file(ad_path)
    final_path = gen_file_path(file_path, md_path)
    gen_md_content(content, ad_content, final_path)


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def find_content_by_tag(content, target_tag):
    els = []
    for obj in content:
        if obj['tag'] == target_tag:
            els.append(obj['content'])
    return els


def gen_file_path(file_path, md_path):
    file_name = os.path.basename(file_path).replace(".json", ".md")
    return os.path.join(md_path, file_name)


def process(match):
    return match.group(1)[:-1] + " "


def gen_md_content(content, ad_content, final_path):
    titles = find_content_by_tag(content, 'title')
    subtitles = find_content_by_tag(content, 'subtitle')
    bodies = find_content_by_tag(content, 'main')
    links = find_content_by_tag(content, 'link')
    md_content = ''
    for title in titles:
        if len(title.strip()) != 0:
            md_content += '# ChatGPT帮我写作之 ' + translate(title) + "\n"
    for subtitle in subtitles:
        if len(subtitle.strip()) != 0:
            md_content += '## ' + translate(subtitle) + "\n"
    for body in bodies:
        if len(body.strip()) != 0:
            translated_content = translate(html2text.html2text(body))
            md_content += re.sub(r"(#+)(?!.*#)", process, translated_content) + "\n"
    for link in links:
        if len(link.strip()) != 0:
            md_content += link + "\n"
    md_content += ad_content
    with open(final_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
