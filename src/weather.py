import os
import requests
from user import User

# print(os.environ.get('WEATHER_API'))
# print(os.environ.get('TEST_PASS'))

user1 = User('Josh', 'Nijjar', 600, 'BBC Business', ['MSFT'], 'GU15',
             'joshnijjar@gmail.com')

url = f"http://api.weatherapi.com/v1/forecast.json?key={os.environ.get('WEATHER_API')}&q={user1.location}&days=1&aqi=no&alerts=no"

def get_weather(url):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
        
def format_weather_data(url):
    """Format the response data from the weather API"""

    data = get_weather(url)

    if data:
        weather = {
            'Location': data['location']['name'],
            'Current Temperature': data['current']['temp_c'],
            'Current Condition': data['current']['condition']['text'],
            'Chance of Rain': data['forecast']['forecastday'][0]['day']['daily_chance_of_rain'],
            'Humidity': data['current']['humidity'],
            'Wind Speed': data['current']['wind_mph'],
            'Feels Like': data['current']['feelslike_c'],
            'Visibility': f"{str(data['current']['vis_km'])} KM",
        }

        return weather
    
def format_weather_text(url):
    weather = format_weather_data(url)

    weather_str = f"""
WEATHER IN {weather['Location']}:
- Current Temperature: {weather['Current Temperature']}°C (Feels Like {weather['Feels Like']}°C)
- Condition: {weather['Current Condition']}
- Chance of Rain: {weather['Chance of Rain']}%
- Wind Speed: {weather['Wind Speed']} km/h
- Visibility: {weather['Visibility']}
"""
    
    return weather_str

def format_weather_html(url):
    weather = format_weather_data(url)

    weather_str = f"""
        <h4>Weather in {weather['Location']}:</h4>
        <ul>
            <li><strong>Current Temperature:</strong> {weather['Current Temperature']}°C (Feels Like {weather['Feels Like']}°C)</li>
            <li><strong>Condition:</strong> {weather['Current Condition']}</li>
            <li><strong>Chance of Rain:</strong> {weather['Chance of Rain']}%</li>
            <li><strong>Wind Speed:</strong> {weather['Wind Speed']} km/h</li>
            <li><strong>Visibility:</strong> {weather['Visibility']}</li>
        </ul>
        """
    
    return weather_str


# print(format_weather_data(get_weather(url)))
