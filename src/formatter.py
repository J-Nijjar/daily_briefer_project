# import utils.helper as helper
from news_feed import get_news_feed
from portfolio_status import show_watchlist
import user
import pprint
import datetime

# def hello():
#    return "Hello world"

# print(hello())
# print(helper.goodbye())

user1 = user.User('Josh', 'Nijjar')

def formatter(user, news_pref):

   brief = f"Hello {user.fullname()}, here's a brief summary of the day \
      {datetime.datetime.now()}:\
      Headlines:\
         {get_news_feed(news_pref)}\
      Portfolio Updates:\
         {show_watchlist(['MSFT', 'FTNT', 'ANET'])}"
   

   return brief

pprint.pp(formatter(user1, 'BBC Business'))