import os
import json


def read_file(file_path, json_file):
    if json_file:
        with open(file_path, 'r') as f:
            return json.load(f)
    with open(file_path, 'r') as file:
        return file.read()


def save_file(file_dir, file_name, content, json_file):
    create_dir(file_dir)
    final_path = os.path.join(file_dir, file_name)
    if json_file:
        with open(final_path, "w", encoding='utf-8') as f:
            f.write(json.dumps(content, ensure_ascii=False, indent=4))
    else:
        with open(final_path, 'w', encoding='utf-8') as f:
            f.write(content)


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
