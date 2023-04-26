from sender.wechat.WechatSender import WechatSender


def execute(root_path):
    ids = WechatSender().retrieve_10_articles_id()
    WechatSender().remove_materials(ids)
