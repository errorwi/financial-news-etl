import yfinance as yf

def fetch_stock_prices(ticker="AAPL"):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1mo")
    df.reset_index(inplace=True)
    return df