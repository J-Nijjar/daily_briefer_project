import yfinance as yf
# from user import User

# user = User("Josh", "Nijjar")

# tickers = yf.Tickers(f"{user.stock_watchlist('MSFT' 'FTNT')}")



# print(f"""{tickers.info['symbol']}
# {tickers.info['currentPrice']}
# {tickers.info['regularMarketChangePercent']}"
# """)
      
def show_watchlist(stock_list):
    
    stock_string = ""

    for stock in stock_list:
        stock_string = stock_string + " " + stock

    tickers = yf.Tickers(stock_string)

    watchlist_info = []

    for stock in stock_list:
        watchlist_info.append([
            stock,
            tickers.tickers[stock].info['currentPrice'],
            f"{tickers.tickers[stock].info['regularMarketChangePercent']}%",
        ])
        
    

    return watchlist_info

def watchlist_as_text(stock_list):
    stock_result = show_watchlist(stock_list)

    stock_text = ""

    if not stock_result:
        return ""
    else:
        
        portfolio_str = "\n".join([
            f" {ticker} | {price} | {change} |" for ticker, price, change in stock_result
    ])
        return portfolio_str

def watchlist_as_html(stock_list):
    stock_result = show_watchlist(stock_list)

    stock_html = ""

    if not stock_result:
        return ""
    else:
        
        stock_html += "<table style='width:100%; border-collapse: collapse;'>"
        stock_html += "<tr><th style='text-align:left; padding: 8px; background-color: #f2f2f2;'>Ticker</th>"
        stock_html += "<th style='text-align:left; padding: 8px; background-color: #f2f2f2;'>Price</th>"
        stock_html += "<th style='text-align:left; padding: 8px; background-color: #f2f2f2;'>Change (%)</th></tr>"

        for stock in stock_result:
            ticker = stock[0]
            price = stock[1]
            prct_chng = stock[2]

            stock_html += f"<tr style='border-bottom: 1px solid #ddd;'>"
            stock_html += f"<td style='padding: 8px;'>{ticker}</td>"
            stock_html += f"<td style='padding: 8px;'>${price}</td>"
            stock_html += f"<td style='padding: 8px;'>{prct_chng}</td>"
            stock_html += "</tr>"

        stock_html += "</table>"

    return stock_html


# print(show_watchlist(['MSFT', 'FTNT', 'ANET']))