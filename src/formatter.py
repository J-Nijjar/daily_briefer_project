# import utils.helper as helper
from news_feed import (get_news_feed, get_news_feed_as_plain_text,
                       get_news_feed_as_html)

from portfolio_status import (show_watchlist, watchlist_as_text,
                              watchlist_as_html)

from google_calendar import get_meetings_as_plain_text, get_meetings_as_html
from quote_of_day import get_quote, html_quote
from weather import (get_weather, format_weather_data, format_weather_text,
                     format_weather_html)

import user
import pprint
import datetime
import os

# def hello():
#    return "Hello world"

# print(hello())
# print(helper.goodbye())

user1 = user.User('Josh', 'Nijjar', 600, 'BBC Business', ['ANET'], 'GU15',
                  'joshnijjar@gmail.com')
url = f"http://api.weatherapi.com/v1/forecast.json?key={os.environ.get('WEATHER_API')}&q={user1.location}&days=1&aqi=no&alerts=no"

def plain_text_formatter(user):
    """Generates a formatted plain-text daily briefing for the user."""

    email_body = f"""
Good Morning, {user.first}!

Here's a brief summary of your day:

📅 SCHEDULE:

{get_meetings_as_plain_text()}

🌥️ WEATHER:
{format_weather_text(url)}

📰 HEADLINES:

{get_news_feed_as_plain_text(user.news_pref)}

📈 PORTFOLIO UPDATES:

{watchlist_as_text(user.stock_list)}

💬 QUOTE OF THE DAY:

{get_quote()}
    """.strip()

    return email_body

def html_formatter(user):
    """Generates a formatted HTML daily briefing for the user."""

    email_body = f"""
    <html>
      <body>
        <h1>Good Morning, {user.first}!</h1>
        <h2>Here's a brief summary of your day:</h2>

        <h2>📅 SCHEDULE:</h2>
        <ul>
          {get_meetings_as_html()}
        </ul>

        <h2>🌥️ WEATHER:</h2>
        <p>{format_weather_html(url)}</p>

        <h2>📰 HEADLINES:</h2>
        <ul>
          {get_news_feed_as_html(user.news_pref)}
        </ul>

        <h2>📈 PORTFOLIO UPDATES:</h2>
        <ul>
          {watchlist_as_html(user.stock_list)}
        </ul>

        <h2>💬 QUOTE OF THE DAY:</h2>
        <p>{html_quote()}</p>

      </body>
    </html>
    """

    return email_body

# pprint.pp(plain_text_formatter(user1))
# pprint.pp(html_formatter(user1))