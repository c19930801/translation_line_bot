# 用於使用 Google 翻譯服務進行文本翻譯。
from googletrans import Translator  # Google 翻譯模組


def translate_text(text, dest='en'):
  # 此啟動此模組翻譯服務的做法
  translator = Translator()
  result = translator.translate(text, dest).text
  return result
