import pandas as pd
import yfinance as yf
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
# top_10_growth_stocks = [('AAPL', 33.5), ('MSFT', 27.8), ('GOOGL', 45.2)]

def get_sp500_tickers(limit=10):
    """Fetch the S&P 500 ticker symbols from Wikipedia and limit the list to the first 'limit' tickers."""
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    table = pd.read_html(url, header=0)
    sp500_tickers = table[0]['Symbol'].tolist()
    return sp500_tickers[:limit]

def fetch_historical_data(tickers):
    """Download the past year's historical data for each ticker."""
    data = yf.download(tickers, period="1y", group_by='ticker')
    return data

def calculate_growth(data, tickers):
    """Calculate the year-over-year growth for each stock."""
    growth_rates = {}
    for ticker in tickers:
        if ticker in data.columns.levels[1]:  # Check if ticker data is present
            start_price = data[ticker]['Adj Close'].iloc[0]
            end_price = data[ticker]['Adj Close'].iloc[-1]
            growth_rate = ((end_price - start_price) / start_price) * 100
            growth_rates[ticker] = growth_rate
    return growth_rates

def top_growth_stocks(growth_rates, top_n=10):
    """Identify the top N growth stocks."""
    sorted_growth = sorted(growth_rates.items(), key=lambda x: x[1], reverse=True)
    return sorted_growth[:top_n]

# Assuming get_sp500_tickers() and other functions are defined as before

# if __name__ == "__main__":
#     # Use a small, known list of tickers for testing
#     test_tickers = ['AAPL', 'MSFT', 'AMZN']
#     historical_data = fetch_historical_data(test_tickers)
#     growth_rates = calculate_growth(historical_data, test_tickers)
#     print(f"Growth Rates: {growth_rates}")  # Debug: print the growth rates
    
#     top_10_growth_stocks = top_growth_stocks(growth_rates)
#     if not top_10_growth_stocks:
#         print("No top growth stocks found.")
#     else:
#         print("Top 10 Growth Stocks:")
#         for ticker, growth in top_10_growth_stocks:
#             print(f"{ticker}: {growth:.2f}% growth")

if __name__ == "__main__":
    sp500_tickers = get_sp500_tickers()
    historical_data = fetch_historical_data(sp500_tickers)
    growth_rates = calculate_growth(historical_data, sp500_tickers)
    top_10_growth_stocks = top_growth_stocks(growth_rates)
    print("Top 10 S&P 500 Growth Stocks:")
    print(top_10_growth_stocks)
    for ticker, growth in top_10_growth_stocks:
        print(f"{ticker}: {growth:.2f}% growth")
