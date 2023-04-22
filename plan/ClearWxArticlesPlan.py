from sender.wechat.WechatSender import WechatSender


def execute(root_path):
    ids = WechatSender().retrieve_all_articles_id()
    WechatSender().remove_materials(ids)
