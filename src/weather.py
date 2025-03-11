import os
import requests
from user import User

# print(os.environ.get('WEATHER_API'))
# print(os.environ.get('TEST_PASS'))

user1 = User('Josh', 'Nijjar', 600, 'BBC Business', ['MSFT'], 'GU15')

url = f"http://api.weatherapi.com/v1/forecast.json?key={os.environ.get('WEATHER_API')}&q={user1.location}&days=1&aqi=no&alerts=no"

def get_weather(url):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
        
    

def format_weather_data(data):
    """Format the response data from the weather API"""


    if data:
        weather = {
            'Location': data['location']['name'],
            'Current Temperature': data['current']['temp_c'],
            'Current Condition': data['current']['condition']['text'],
            'Chance of Rain': data['forecast']['forecastday'][0]['day']['daily_chance_of_rain'],
            'Humidity': data['current']['humidity'],
            'Wind Speed': data['current']['wind_mph'],
            'Feels Like': data['current']['feelslike_c'],
            'Visibility': f"{str(data['current']['vis_km'])}KM",
        }

        return weather

print(format_weather_data(get_weather(url)))
