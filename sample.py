from flask import Flask, request
import requests

app = Flask(__name__)

# تنظیمات برای ربات بله
BOT_TOKEN = '1811623771:iA5TFugS5sUTWl41nvHQNp5H6FjOQ2Y2mbZhmy8Y'
BOT_URL = f'https://api.bale.ai/{BOT_TOKEN}/'

# رویداد برای دریافت پیام‌ها از بله
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data['message']['text']
    chat_id = data['message']['chat']['id']
    
    # پاسخ را از بله دریافت کنید
    response = get_bale_response(message)
    
    # ارسال پاسخ به بله
    send_bale_message(chat_id, response)
    
    return 'OK'

# تابع برای دریافت پاسخ از بله
def get_bale_response(message):
    response = requests.get(BOT_URL + 'sendMessage', params={'text': message})
    data = response.json()
    return data['result']['text']

# تابع برای ارسال پیام به بله
def send_bale_message(chat_id, message):
    requests.get(BOT_URL + 'sendMessage', params={'chat_id': chat_id, 'text': message})

if __name__ == '__main__':
    app.run()
    send_bale_message(chat_id="1811623771",message="salam")
