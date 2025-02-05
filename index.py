from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Fix lỗi CORS

API_KEY = "392b44d861bff9b6fac2585893b51903"  # Thay thế bằng API Key mới

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Vui lòng nhập tên thành phố!"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"],  # Lấy mã icon
        }
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Không thể lấy dữ liệu thời tiết!"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
