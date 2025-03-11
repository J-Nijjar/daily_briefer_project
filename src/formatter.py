# import utils.helper as helper
from news_feed import get_news_feed
from portfolio_status import show_watchlist
from google_calendar import get_meetings, get_credentials
from weather import get_weather, format_weather_data
import user
import pprint
import datetime
import os

# def hello():
#    return "Hello world"

# print(hello())
# print(helper.goodbye())

user1 = user.User('Josh', 'Nijjar', 600, 'BBC Business', ['ANET'], 'GU15')
url = f"http://api.weatherapi.com/v1/forecast.json?key={os.environ.get('WEATHER_API')}&q={user1.location}&days=1&aqi=no&alerts=no"

def formatter(user, news_pref):
    """Generates a formatted daily briefing for the user."""
    
    return (
        f"Good Morning {user.fullname()}, here's a brief summary of your day:\n\n"
        f"📅 Schedule:\n{get_meetings()}\n\n"
        f"🌥️ Weather:\n{format_weather_data(get_weather(url))}"
        f"📰 Headlines:\n{get_news_feed(news_pref)}\n\n"
        f"📈 Portfolio Updates:\n{show_watchlist(['MSFT', 'FTNT', 'ANET'])}"
    )


pprint.pp(formatter(user1, 'BBC Business'))