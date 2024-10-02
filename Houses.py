import requests
from bs4 import BeautifulSoup

def scrape_housing_prices(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find elements containing housing price information
        prices = soup.find_all('div', class_='price')  # Adjust class name as per the target website
        
        # Extract and print the housing prices
        for price in prices:
            print(price.text.strip())  # Modify this according to the structure of the webpage
    else:
        print("Failed to retrieve data from the website")

# URL of the real estate website in North Carolina
url = "https://www.redfin.com/"

# Call the function to scrape housing prices
scrape_housing_prices(url)
