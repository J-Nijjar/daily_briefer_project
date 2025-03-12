import os
import requests

def get_quote():
    """Gets a daily quote"""
    url = "https://zenquotes.io/api/random"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
    else:
        return "Error retrieving API"
    
    quote = f"'{data[0]['q']}'" + " - " + data[0]['a']
    
    return quote

def html_quote():
    html_q = get_quote()

    if not html_q:
        quote = """<p style="font-size: 18px; font-family: Arial, sans-serif; color: #333;">
                 "Freedom is the only worthy goal in life. It is won by disregarding things that lie beyond our control."
                 <br><em>- Epictetus</em>
               </p>"""
        return quote
    
    else:
        return f"<h3>{html_q}</h3>"
    

# print(get_quote())