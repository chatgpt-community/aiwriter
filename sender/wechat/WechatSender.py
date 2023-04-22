import os
import requests
import json


class WechatSender:
    def __init__(self):
        self.app_id = os.environ.get('wechat_appid')
        self.app_secret = os.environ.get('wechat_secret')

    def send(self, event):
        if not self.app_id or not self.app_secret:
            print("Error: wechat_appid and/or wechat_secret not set.")
            raise ValueError("Missing required environment variables.")

        access_token = self.get_access_token()

        # Add draft article
        add_draft_url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        replaced_img_content = event['content'].replace('PLACE_HOLDER',
                                                        'https://mmbiz.qpic.cn/mmbiz_jpg/dghhiacNqQgg5Ub3OWHhU4cAIIZeooEfF6Ivicx3yyklokrsW3NIdgtibSVlNMdGTPJsvkuFrWnicbiarHiaiaX0Zy8jg/0?wx_fmt=jpeg')
        add_draft_data = {
            "articles": [{
                "title": event['title'],
                "thumb_media_id": "HQ85pONUeuAHlOhfVuNPhLcEt8TC8zH_EF9M-AiaMxqU91VJ_e2vCwDxCSlJHtwp",
                "author": "熊大",
                "digest": event['subTitle'],
                "content": replaced_img_content,
                "content_source_url": event['sourceLink'],
                "need_open_comment": 0,
                "only_fans_can_comment": 0
            }]
        }
        add_draft_response = requests.post(add_draft_url, headers=headers,
                                           data=bytes(json.dumps(add_draft_data, ensure_ascii=False), encoding='utf-8'))
        result = json.loads(add_draft_response.text)
        media_id = result['media_id']

        # Publish draft article
        publish_url = f"https://api.weixin.qq.com/cgi-bin/freepublish/submit?access_token={access_token}"
        publish_data = {
            "media_id": media_id
        }
        requests.post(publish_url, json=publish_data)

        # Log media_id of published article
        print(f"Published article with media_id: {media_id}")
        return media_id

    def retrieve_all_articles_id(self):
        access_token = self.get_access_token()
        article_ids = []
        current_count = 20
        offset = 0
        while current_count == 20:
            batch_get_url = f'https://api.weixin.qq.com/cgi-bin/freepublish/batchget?access_token={access_token}'
            batch_get_body = {
                "offset": offset,
                "count": current_count
            }
            response = requests.post(batch_get_url, json=batch_get_body)
            result = json.loads(response.text)
            current_count = result['item_count']
            offset += current_count
            for i in result['item']:
                article_ids.append(i['article_id'])
        return article_ids

    def remove_materials(self, ids):
        access_token = self.get_access_token()
        remove_article_url = f'https://api.weixin.qq.com/cgi-bin/freepublish/batchget?access_token={access_token}'
        for a_id in ids:
            print('Current id: ' + a_id)
            body = {
                "article_id": a_id,
            }
            response = requests.post(remove_article_url, json=body)
            remove_res = json.loads(response.text)
            if remove_res['errcode'] == 0:
                print('Remove successfully!')
            else:
                print(f'Remove failed!, code:{remove_res["errcode"]}, message: {remove_res["errmsg"]}')

    def get_access_token(self):
        # Get access token
        token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        token_response = requests.get(token_url)
        token_data = json.loads(token_response.text)
        access_token = token_data['access_token']
        return access_token
