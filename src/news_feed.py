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
    
        
    
    else:
        return f"Not supported by provider: {provider}"
    
    return list_entries

def get_news_feed_as_plain_text(provider):
    news_result = get_news_feed(provider)

    news_text = ""

    if not news_result:
        news_text = "- There are no headlines for today"
        return news_text
    
    else:
        headlines_str = "\n".join([
        f"- {title}\n   {summary}\n     {link}" for title, summary, link in news_result
    ])
        
    return headlines_str
        
def get_news_feed_as_html(provider):
    news_result = get_news_feed(provider)

    news_html = ""

    if not news_result:
        news_html = "<li>There are no headlines for today</li>"
    else:
        for news in news_result:
            title = news[0]
            desc = news[1]
            link = news[2]
            news_html += f"""
            <li>
                <a href="{link}" target="_blank"><strong>{title}</strong></a><br>
                <em>{desc}</em>
            </li>
            """
    return news_html
    
            
# entries = get_news_feed('BBC')
# print(entries)




