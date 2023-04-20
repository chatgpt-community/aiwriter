import os
import requests
import json


class WechatSender:
    def __init__(self):
        self.app_id = os.environ.get('wechat_appid')
        self.app_secret = os.environ.get('wechat_secret')

    def send(self, event):
        print(self.app_secret)
        print(self.app_id)
        if not self.app_id or not self.app_secret:
            print("Error: wechat_appid and/or wechat_secret not set.")
            raise ValueError("Missing required environment variables.")

        # Get access token
        token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        token_response = requests.get(token_url)
        token_data = json.loads(token_response.text)
        access_token = token_data['access_token']

        # Add draft article
        add_draft_url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}"

        add_draft_data = {
            "articles": [{
                "title": event['title'],
                "thumb_media_id": "HQ85pONUeuAHlOhfVuNPhLcEt8TC8zH_EF9M-AiaMxqU91VJ_e2vCwDxCSlJHtwp",
                "author": "熊大",
                "digest": event['subTitle'],
                "content": event['content'],
                "content_source_url": '',
                "need_open_comment": 0,
                "only_fans_can_comment": 0
            }]
        }
        add_draft_response = requests.post(add_draft_url, json=add_draft_data)
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
