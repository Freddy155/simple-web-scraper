# Web Scraper

This Python script scrapes quotes from a website and prints them. In this example, we scrape quotes from [http://quotes.toscrape.com](http://quotes.toscrape.com).

## Dependencies

- Python 3.x
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Installation

1. Ensure you have Python 3.x installed on your system.

2. Install the required libraries using pip:

    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

1. Clone or download this repository.
   ```bash
   git clone https://github.com/Freddy155/simple-web-scraper.git
   ```

3. Navigate to the project directory:

    ```bash
    cd simple-web-scraper
    ```

4. Run the web scraper script:

    ```bash
    python app.py
    ```

    This will scrape quotes from the target website and print them to the console.

## Customization

To scrape a different website or modify the scraping behavior:

1. Open `app.py` in a text editor.

2. Change the `url` variable to the desired website URL.

3. Modify the code to extract the information you need based on the target website's HTML structure.

4. Run the script to scrape the updated website.

## Disclaimer

Make sure to use this web scraper responsibly and in compliance with the target website's terms of service. Always respect website policies and avoid excessive scraping that could cause strain on the website's servers.
