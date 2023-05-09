from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from pymongo import MongoClient
import re

# This will only need to be ran once
def fetch_all_us_card_info():
    # Configuring options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=Service('path/to/your/chromedriver'), options=chrome_options)

    driver.get('https://okini.land/en/212-pok%C3%A9mon-card-game?in-stock=1')

    scroll_pause_time = 1.2  

    while True:
        # Store page source before scrolling
        old_page = driver.page_source

        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)

        # Store page source after scrolling
        new_page = driver.page_source

        # If nothing has changed in the page source, break the loop
        if new_page == old_page:
            break
            
    # Parse the page HTML with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    product_data = []
    # Find each product div and print the product name, URL, image URL, and price
    for div in soup.find_all('div', {'class': 'thumbnail-container relative'}):
        # Extract the product URL
        product_url = div.find('a', {'class': 'relative'}).get('href')

        # Extract the image URL
        image_tag = div.find('img', {'class': 'smooth05'})
        image_url = image_tag.get('src') if image_tag else None

        # Extract the product title
        product_title = div.find('span', {'class': 'product-title'}).text.strip()

        # Extract the price
        price = div.find('span', {'class': 'price'}).text.strip()
        product_data.append({
                'Product Title': product_title,
                'Product URL': product_url,
                'Image URL': product_image_url,
                'Price': price,
            })
        print(f"Product URL: {product_url}")
        print(f"Image URL: {image_url}")
        print(f"Product Title: {product_title}")
        print(f"Price: {price}")
    # Create a connection to MongoDB
    client = MongoClient("mongodb+srv://admin:admin@cluster0.wj4vxhv.mongodb.net/?retryWrites=true&w=majority")

    # Select the database
    db = client['pokemon_cards']

    # Select the collection within the database
    collection = db['us_cards']

    # Insert the list of dictionaries in the collection
    collection.insert_many(product_data)

# This will only be to be ran once
def update_card_in_english():
  
    # Create a client and connect to your MongoDB instance
    client = MongoClient('mongodb+srv://admin:admin@cluster0.wj4vxhv.mongodb.net/?retryWrites=true&w=majority')
    db = client['pokemon_cards']

    # Get your collections
    collection1 = db['cards']
    collection2 = db['us_cards']

    # Iterate over documents in the first collection
    for doc1 in collection1.find():
        # Get the unique_id and convert it to lowercase
        unique_id = doc1['unique_id'].replace('-', '').replace('>', '').lower()

        # Iterate over documents in the second collection
        for doc2 in collection2.find():
            # Get the product_title, convert it to lowercase, and split it
            product_title = doc2['Product Title']
            cleaned_product_title = re.sub('[^a-zA-Z0-9]', '', product_title).lower()
            parts = product_title.split(' - ')

            # If unique_id is in product_title and product_title has at least 3 parts
            if unique_id in cleaned_product_title and len(parts) >= 3:
                # Get the last part of the product_title
                part3 = parts[-1]

                # Get the image URL from the document in the second collection
                image_url = doc2['Image URL']

                # Update the document in the first collection with the new US_name and Image URL
                collection1.update_one({'_id': doc1['_id']}, {'$set': {'US_name': part3, 'Image URL': image_url}})



# This is the active scripts that updates prices in USD, run this function whenever we needs to update card prices in USD
def update_us_price():
    url = "https://www.pricecharting.com/game/pokemon-japanese-vstar-universe/"

    # Create a client and connect to your MongoDB instance
    client = MongoClient('mongodb+srv://admin:admin@cluster0.wj4vxhv.mongodb.net/?retryWrites=true&w=majority')
    db = client['pokemon_cards']

    # Get your collections
    collection1 = db['cards']

    # Iterate over documents in the first collection
    for doc1 in collection1.find():
        # Get the unique_id and convert it to lowercase
        unique_id = doc1['_id']
        id = "S12a-015>172"
        # Use split() to divide the string into parts based on '-'
        parts = unique_id.split('-')
        if "S8a-P" not in unique_id:
            # Get the middle part and split it again based on '>'
            card_digit = int(parts[1].split('>')[0])
            card_digit = str(card_digit)
            card_name = doc1['US_name']
        else:
            card_digit = int(parts[2].split('>')[0])
            card_digit = str(card_digit)
            card_name = doc1['US_name']
            
        if card_name == "":
            continue
        
        card_name = card_name.replace(" ", "-")
        query = card_name + "-" + card_digit
        url = url + query
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        price_text = soup.find('span', class_='price js-price')
        if price_text is None or price_text.text.strip() == "N/A":
            collection1.update_one({'_id': doc1['_id']}, {'$set': {'US_price': "N/A"}})
            url = "https://www.pricecharting.com/game/pokemon-japanese-vstar-universe/"
            continue

        # Since the price_text now contains "$10.22\n", we use strip() to remove the leading/trailing whitespace
        price_text = price_text.text.strip()

        price = float(price_text.replace('$', ''))
        collection1.update_one({'_id': doc1['_id']}, {'$set': {'US_price': price}})
        url = "https://www.pricecharting.com/game/pokemon-japanese-vstar-universe/"
            


def update_some_us_price(cards_by_us_name):
    url = "https://www.pricecharting.com/game/pokemon-japanese-vstar-universe/"

    # Create a client and connect to your MongoDB instance
    client = MongoClient('mongodb+srv://admin:admin@cluster0.wj4vxhv.mongodb.net/?retryWrites=true&w=majority')
    db = client['pokemon_cards']

    # Get your collections
    collection1 = db['cards']

    # Iterate over the provided list of US name cards
    for card_name in cards_by_us_name:
        # Find the corresponding document in the collection
        doc1 = collection1.find_one({'US_name': card_name})
        
        if doc1 is None:
            print(f"Card not found: {card_name}")
            continue

        # Get the unique_id
        unique_id = doc1['_id']

        # Use split() to divide the string into parts based on '-'
        parts = unique_id.split('-')
        
        if "S8a-P" not in unique_id:
            # Get the middle part and split it again based on '>'
            card_digit = int(parts[1].split('>')[0])
            card_digit = str(card_digit)
        else:
            card_digit = int(parts[2].split('>')[0])
            card_digit = str(card_digit)

        card_name = card_name.replace(" ", "-")
        query = card_name + "-" + card_digit
        url = url + query
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        price_text = soup.find('span', class_='price js-price')
        
        if price_text is None or price_text.text.strip() == "N/A":
            collection1.update_one({'_id': doc1['_id']}, {'$set': {'US_price': "N/A"}})
            url = "https://www.pricecharting.com/game/pokemon-japanese-vstar-universe/"
            continue

        # Since the price_text now contains "$10.22\n", we use strip() to remove the leading/trailing whitespace
        price_text = price_text.text.strip()

        price = float(price_text.replace('$', ''))
        collection1.update_one({'_id': doc1['_id']}, {'$set': {'US_price': price}})
        url = "https://www.pricecharting.com/game/pokemon-japanese-vstar-universe/"



