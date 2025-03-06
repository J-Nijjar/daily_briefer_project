import requests
import json
import feedparser

feeds = {
    'BBC': "https://feeds.bbci.co.uk/news/rss.xml?edition=uk",
    'Guardian': 'http://www.guardian.co.uk/rss/0,,,00.xml',
    'BBC Business':
    'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/business/rss.xml',
    'Fake-RSS': "http://fake-rss-url.com",
    # 'Yahoo': 'http://rss.news.yahoo.com/rss/topstories',

}

def get_news_feed(provider):
    if provider in feeds.keys():

        r = feedparser.parse(feeds[provider])
        r = r.entries

        list_entries = []

        for i, entry in enumerate(r):
            if i <= 3:
                try:
                    list_entries.append([entry.title, 
                                        entry.description, entry.link])
                except AttributeError as e:
                    print(e)
            
            else:
                break
    
        return list_entries
    
    else:
        return f"Not supported by provider: {provider}"
    
            
# entries = get_news_feed('BBC')
# print(entries)




