# Fetch and display weather information for a specific city.

def get_weather(city):
    api_key = 'your_api_key'  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    
    if response.get('main'):
        return response['main']
    else:
        return "City not found."

city_name = input("Enter city name: ")
print(get_weather(city_name))
