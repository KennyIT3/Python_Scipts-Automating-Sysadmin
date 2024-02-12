import yfinance as yf
import time

def monitor_stock(symbol, interval=10):
    while True:
        stock = yf.Ticker(symbol)
        info = stock.info
        price = info.get("ask", "N/A")
        low_52_weeks = info.get("fiftyTwoWeekLow", "N/A")
        high_52_weeks = info.get("fiftyTwoWeekHigh", "N/A")

        print(f"{symbol} Stock Price: {price}")
        print(f"52-Week Low: {low_52_weeks} | 52-Week High: {high_52_weeks}")
        print("\n")
        time.sleep(interval)

if __name__ == "__main__":
    stock_symbol = "ORLY"  # O'Reilly Automotive, Inc.
    monitor_stock(stock_symbol)


#Now, the script will display both the current stock price and the 52-week low and high values. Adjust the `interval` parameter as needed for the frequency of updates.