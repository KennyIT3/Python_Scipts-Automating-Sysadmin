import yfinance as yf
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def get_sp500_tickers(limit=100):
    """Fetch the S&P 500 ticker symbols from Wikipedia and limit the list to the first 'limit' tickers."""
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    table = pd.read_html(url, header=0)
    sp500_tickers = table[0]['Symbol'].tolist()
    return sp500_tickers[:limit]

def fetch_stocks_data(tickers):
    """
    Fetch historical stock data for the given tickers.
    """
    data = yf.download(tickers, start="2023-01-01", end="2024-01-01")['Adj Close']
    return data

def calculate_growth(stocks_data):
    """
    Calculate the YoY growth percentage for each stock.
    """
    growth = ((stocks_data.iloc[-1] - stocks_data.iloc[0]) / stocks_data.iloc[0]) * 100
    return growth.sort_values(ascending=False)

def list_top_growth_stocks(tickers, top_n=100):
    """
    List the top N growth stocks based on YoY price increase percentage.
    """
    stocks_data = fetch_stocks_data(tickers)
    growth = calculate_growth(stocks_data)

    print(f"Top {top_n} Growth Stocks of 2024:")
    for ticker, growth_pct in growth.head(top_n).items():
        print(f"{ticker}: {growth_pct:.2f}% growth")

if __name__ == "__main__":
    sp500_tickers = get_sp500_tickers()
    list_top_growth_stocks(sp500_tickers)
