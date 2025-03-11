

class User:
    """An object representing the user it's working with.
    """

    def __init__(self, first, last, alarm, news_pref, stock_list, location):
        self.first = first
        self.last = last
        self.alarm = alarm
        self.news_pref = news_pref
        self.stock_list = stock_list
        self.location = location

        
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def alarm_time(self, alarm):
        return f"{self.first}, wakes up at {alarm}."
    
    def news_preference(self, news):
        return news
    
    def stock_watchlist(self, stocks):
        return stocks
    

# user1 = User("Josh", "Nijjar")

# print(user1.fullname())
# print(user1.alarm_time("6:00am"))


