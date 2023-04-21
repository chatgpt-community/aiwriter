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

        # Get access token
        token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        token_response = requests.get(token_url)
        token_data = json.loads(token_response.text)
        access_token = token_data['access_token']

        media_url = f"https://api.weixin.qq.com/cgi-bin/material/get_material?access_token={access_token}"
        add_draft_response = requests.post(media_url, {
            'media_id': ''})

        # Add draft article
        add_draft_url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        replaced_img_content = event['content'].replace('PLACE_HOLDER', 'https://mmbiz.qpic.cn/mmbiz_jpg/dghhiacNqQgg5Ub3OWHhU4cAIIZeooEfF6Ivicx3yyklokrsW3NIdgtibSVlNMdGTPJsvkuFrWnicbiarHiaiaX0Zy8jg/0?wx_fmt=jpeg')
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
        publish_response = requests.post(publish_url, json=publish_data)

        # Log media_id of published article
        print(f"Published article with media_id: {media_id}")
        return media_id
