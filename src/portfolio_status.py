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




# print(show_watchlist(['MSFT', 'FTNT', 'ANET']))