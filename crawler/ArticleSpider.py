import json
import subprocess

# Step 1: Run Gpt3DemoArticleLinksSpider.py
subprocess.run(['python3.11', 'Gpt3DemoArticleLinksSpider.py'])

# Step 2: Parse articleList.json and retrieve list of articles
with open('articleList.json', 'r') as f:
    article_data = json.load(f)
article_list = article_data['articles']

# Step 3: Traverse list and run Gpt3DemoArticleSpider.py for each article
for article in article_list:
    subprocess.run(['python3.11', 'Gpt3DemoArticleSpider.py', article])
