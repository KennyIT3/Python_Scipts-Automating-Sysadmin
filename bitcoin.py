import requests

def track_bitcoin_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = response.json()
    price = data['bpi']['USD']['rate']
    print(f"The current Bitcoin price is {price} USD")

track_bitcoin_price()