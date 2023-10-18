import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "http://quotes.toscrape.com"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extract and print the text of all the quotes on the page
    quotes = soup.find_all('span', class_='text')
    
    for quote in quotes:
        print(quote.get_text())
else:
    print("Failed to retrieve the page. Status code:", response.status_code)

