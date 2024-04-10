# Flask 是一個 Python Web 框架，用於構建 Web 應用程式。
# request 它被用於處理來自 LINE 平台的請求
# abort 模組用於在 Flask 應用程式中處理錯誤和異常情況。
from flask import Flask, request, abort
# LineBotApi 是一個用於與 LINE 平台 API 進行通信的 Python 客戶端庫。
# WebhookHandler 是用於處理 LINE Bot 的 Webhook 的類
from linebot import (LineBotApi, WebhookHandler)
# 用於處理來自 LINE 平台的無效簽名錯誤。
from linebot.exceptions import (InvalidSignatureError)
# 這些是 LineBot 的模型類，用於表示 LINE 平台的事件和消息。
# MessageEvent 用於表示各種類型的消息事件，TextMessage 用於表示文本消息，TextSendMessage 用於表示發送給用戶的文本消息。
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
# 用於使用 Google 翻譯服務進行文本翻譯。
from googletrans import Translator  # Google 翻譯模組
# 用於存儲配置信息，例如 LINE Bot 的認證密鑰、Google 翻譯服務的設置等。
from config import *
from my_commands.translate_text import translate_text
from my_commands.bot_gpt import get_reply
import re
import os

app = Flask(__name__)

# 透過'LINE_TOKEN'和'LINE_SECRET'來建立 LineBotApi 的物件與WebhookHandler 物件以便後續的訊息接收和發送訊息正確執行
api = LineBotApi(os.getenv('LINE_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_SECRET'))
# 初始化Flask應用程式,這是Flask運作的核心.app會根據設定的路由和對應的涵式來處理HTTP請求
app = Flask(__name__)


@app.route("/")
def hello():
  return "萬國機器人上限囉!"


  # 設定當收到"/"路徑的post請求時,自動執行下方的callback()涵式,通道會透過這個方式將使用者輸入的訊息轉送過來
@app.post("/")
def callback():
  # 取得 X-Line-Signature 表頭電子簽章內容
  # Line傳送過來的電子簽章.由於這個電子簽章式已建立通道時取得的密鑰為基準,可以篩選不是由我的通道送來的請求
  signature = request.headers['X-Line-Signature']

  # 以文字形式取得請求內容
  # 以文字形式取的請求內容並透過app來記錄,這會在稍後驗證電子簽章時使用
  body = request.get_data(as_text=True)
  app.logger.info("Request body: " + body)

  # 比對電子簽章並處理請求內容
  # 以剛剛取得的請求內容及表頭中的電子簽章進行驗證,電子簽章驗證錯誤會拋出例外訊息;驗證正確,則會自動呼叫稍後設定的處理涵式
  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    print("電子簽章錯誤, 請檢查密鑰是否正確？")
    abort(400)

  return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  if event.source.user_id == 'Udeadbeefdeadbeefdeadbeefdeadbeef':
    return 'OK'
  user_message = event.message.text
  # 翻譯英文
  if re.match('@英文', user_message):
    content = translate_text(event.message.text[3:], "en")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)

  # 翻譯日文
  elif re.match('@日文', user_message):
    content = translate_text(event.message.text[3:], "ja")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)

  # 翻譯中文
  elif re.match('@中文', user_message):
    content = translate_text(event.message.text[3:], "zh-tw")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)

  # 翻譯泰文
  elif re.match('@泰文', user_message):
    content = translate_text(event.message.text[3:], "th")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)

  # 翻譯土耳其文
  elif re.match('@土耳其語', user_message):
    content = translate_text(event.message.text[5:], "th")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)
  # 翻譯烏克蘭語
  elif re.match('@烏克蘭語', user_message):
    content = translate_text(event.message.text[5:], "uk")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)
  # 翻譯越南語
  elif re.match('@越南語', user_message):
    content = translate_text(event.message.text[4:], "vi")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)
  # 翻譯俄語
  elif re.match('@俄語', user_message):
    content = translate_text(event.message.text[3:], "ru")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)
  # 翻譯西班牙語
  elif re.match('@西班牙語', user_message):
    content = translate_text(event.message.text[5:], "es")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)
  # 翻譯緬甸語
  elif re.match('@緬甸語', user_message):
    content = translate_text(event.message.text[4:], "my")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)
  # 翻譯韓文
  elif re.match('@韓文', user_message):
    content = translate_text(event.message.text[3:], "ko")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)
  # 翻譯意大利語
  elif re.match('@意大利語', user_message):
    content = translate_text(event.message.text[5:], "it")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)
  # 翻譯德語
  elif re.match('@德語', user_message):
    content = translate_text(event.message.text[3:], "de")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)
  # 翻譯法文
  elif re.match('@法文', user_message):
    content = translate_text(event.message.text[3:], "fr")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)
  # 翻譯芬蘭語
  elif re.match('@芬蘭語', user_message):
    content = translate_text(event.message.text[4:], "fi")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)
  # 翻譯菲律賓語
  elif re.match('@菲律賓語', user_message):
    content = translate_text(event.message.text[5:], "tl")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)
  # 翻譯阿拉伯語
  elif re.match('@阿拉伯語', user_message):
    content = translate_text(event.message.text[5:], "ar")
    message = TextSendMessage(text=content)
    api.reply_message(event.reply_token, message)

  # AI
  elif re.match('ai|Ai|AI', user_message):
    reply_text = get_reply(user_message)
    api.reply_message(event.reply_token, TextSendMessage(text=reply_text))
  else:
    text = "請在輸入文字前加上[@想要輸入的語言]\n ex:@英文 你好啊!"
    api.reply_message(event.reply_token, TextSendMessage(text=text))


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
