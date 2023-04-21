import time

from googletrans import Translator

translator = Translator()


def translate(text):
    time.sleep(0.5)
    try:
        return translator.translate(text, src='en', dest='zh-CN').text
    except Exception as e:
        print("Error: translate error!", e)
        print('-----------------------------')
        print(text)
        print('-----------------------------')
        return ''
