import re


def find_last_word_in_url(url):
    last_slash_pos = url.rfind('/')
    if last_slash_pos != -1:
        return url[last_slash_pos + 1:]


def compress_text(text):
    return ''.join(text.splitlines())


def remove_html_attrs(text):
    return remove_by_pattern(r'\s(class|id|name|style|href)="[^"]*"', text)


def remove_html_comment(text):
    return remove_by_pattern(r"<!--.*?-->", text)


def remove_by_pattern(pattern, text):
    return re.sub(pattern, '', text)


def replace(old, target, new):
    return old.replace(target, new)
