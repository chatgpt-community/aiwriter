from googletrans import Translator

translator = Translator()


def translate(text):
    return translator.translate(text, src='en', dest='zh-CN').text
