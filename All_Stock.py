import yfinance as yf
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd

def monitor_growth_stocks(stock_symbols, days=30, growth_threshold=0.05):
    growth_stocks = []

    for symbol in stock_symbols:
        stock_data = yf.download(symbol, period=f"{days}d")
        closing_prices = stock_data['Close']

        # Calculate percentage change
        percentage_change = (closing_prices[-1] - closing_prices[0]) / closing_prices[0]

        if percentage_change > growth_threshold:
            growth_stocks.append(symbol)

    return growth_stocks

if __name__ == "__main__":
    # Example: Monitor growth stocks in the last 30 days
    stock_symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    growth_stocks = monitor_growth_stocks(stock_symbols)

    if growth_stocks:
        print("Growth stocks:", growth_stocks)
    else:
        print("No growth stocks found.")
