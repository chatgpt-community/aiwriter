import os
import unittest
from unittest.mock import patch
from WechatSender import WechatSender


class TestWechatSender(unittest.TestCase):
    def setUp(self):
        os.environ['wechat_appid'] = 'replace_me'
        os.environ['wechat_secret'] = 'replace_me'

    def tearDown(self):
        if 'wechat_appid' in os.environ:
            del os.environ['wechat_appid']
        if 'wechat_secret' in os.environ:
            del os.environ['wechat_secret']

    # @patch('requests.get')
    # def test_send_successful(self, mock_get):
    #     mock_get.return_value.status_code = 200
    #     mock_get.return_value.json.return_value = {'access_token': 'test_token'}
    #
    #     event = {'title': 'Test Article', 'subTitle': 'Test Subtitle', 'content': 'Test Content'}
    #     sender = WechatSender()
    #     sender.send(event)
    #
    #     self.assertIsNotNone(sender.media_id)
    #     self.assertEqual(mock_get.call_count, 1)

    def test_send_successful(self):
        event = {'title': 'Test Article2', 'subTitle': 'Test Subtitle2', 'content': 'Test Content2'}
        sender = WechatSender()
        media_id = sender.send(event)

        self.assertIsNotNone(media_id)

    def test_missing_credentials(self):
        del os.environ['wechat_appid']

        event = {'title': 'Test Article', 'subTitle': 'Test Subtitle', 'content': 'Test Content'}
        sender = WechatSender()

        with self.assertRaises(ValueError):
            sender.send(event)
