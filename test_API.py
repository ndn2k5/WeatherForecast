import requests

def test_api_key(api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Ho%20Chi%20Minh&appid={api_key}&units=metric"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    print("Response JSON:", response.json())

# Thay thế bằng API Key mới
API_KEY = "392b44d861bff9b6fac2585893b51903"  
test_api_key(API_KEY)
