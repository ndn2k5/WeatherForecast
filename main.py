import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = {     
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
        }
        return weather
    else:
        return {"error": "Không thể lấy dữ liệu thời tiết!"}

if __name__ == "__main__":
    API_KEY = "392b44d861bff9b6fac2585893b51903"  # Thay thế bằng API Key của bạn
    city = input("Nhập tên thành phố: ")
    weather_data = get_weather(city, API_KEY)
    
    if "error" in weather_data:
        print(weather_data["error"])
    else:
        print(f"Thành phố: {weather_data['city']}")
        print(f"Nhiệt độ: {weather_data['temperature']}°C")
        print(f"Độ ẩm: {weather_data['humidity']}%")
        print(f"Mô tả: {weather_data['description']}")