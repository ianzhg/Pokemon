from flask import request, jsonify, Blueprint, Flask
from US_pokemon import update_us_price, update_some_us_price
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
from db import collection
from shipping import function_runner
from shipping import DHL
from shipping import japan_post
from shipping import fedex
from exchangerate import get_exchange_rate

# app = Flask(__name__)
# CORS(app, resources={r"*": {"origins": "*"}})

api = Blueprint('api', __name__, url_prefix='/api')

@api.route("/")
def index():
    return "Hello world"

# Define route to store data in MongoDB
@api.route("/store_data", methods=["POST"])
def store_data():
    data = request.get_json()

    # Insert data into MongoDB with unique_id as the document _id
    result = collection.update_one({"_id": data["unique_id"]}, {"$set": data}, upsert=True)

    # Return response
    return jsonify({"message": "Data stored successfully!", "id": data["unique_id"]})

# Define route to get data from MongoDB by unique_id
@api.route("/get_data/<unique_id>", methods=["GET"])
def get_data(unique_id):
    # Find data in MongoDB by unique_id
    result = collection.find_one({"_id": unique_id})

    if result:
        # Return data if found
        return jsonify({"message": "Data retrieved successfully!", "output": result})
    else:
        # Return error message if not found
        return jsonify({"error": f"No data found for unique_id {unique_id}."})

# Define route to update data in MongoDB by unique_id. This automatically check how many fields to update and update in database
@api.route("/update_data/<unique_id>", methods=["PUT"])
def update_data(unique_id):
    data = request.get_json()

    fields_to_update = {}
    for field, value in data.items():
        if field == "JP_price":
            fields_to_update["JP_price"] = value
        elif field == "JP_name":
            fields_to_update["JP_name"] = value
        elif field == "US_name":
            fields_to_update["US_name"] = value
        elif field == "US_price":
            fields_to_update["US_price"] = value

    if fields_to_update:
        # Update data in MongoDB by unique_id
        result = collection.update_one({"_id": unique_id}, {"$set": fields_to_update})

        if result.modified_count > 0:
            # Return success message if at least one field was updated
            return jsonify({"message": "Data updated successfully!", "id": unique_id})
        else:
            # Return error message if no fields were updated
            return jsonify({"error": f"No fields were updated for unique_id {unique_id}."})
    else:
        # Return error message if no fields were present in the input
        return jsonify({"error": "No fields present in input."})


@api.route("/update_us_price/all", methods=["PUT"])
def update_us_prices_endpoint():
    try:
        update_us_price()
        return jsonify({"message": "Prices updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api.route("/update_us_price", methods=["PUT"])
def update_some_us_prices_endpoint():
    try:
        # Get the JSON object from the request
        data = request.get_json()

        # Get the list of cards from the JSON object
        cards_to_update = data.get("cards")

        if not cards_to_update:
            return jsonify({"error": "No cards provided to update"}), 400

        update_some_us_price(cards_to_update)
        return jsonify({"message": "Prices updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@api.route("/most_volatile_cards", methods=["GET"])
def most_volatile_cards_endpoint():
    ## Get the most hyped data
    url = 'https://pokemonprices.com/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all 'tr' elements
    rows = soup.find_all('tr')

    # Define a list to store the card data
    card_data = []

    # Iterate over each row
    for row in rows:
        # Get all 'td' elements in the row
        tds = row.find_all('td')
        
        # Ensure that there are four 'td' elements in the row
        if len(tds) == 4:
            # Extract the necessary information from each 'td' element
            name = tds[1].find('b').text
            collector_info = tds[1].find_all('br')[0].next_sibling.strip('\n')
            set = tds[1].find_all('a')[1].text.strip('\n')
            rarity = tds[1].find_all('br')[2].next_sibling.strip('\n').strip('()')
            price = tds[2].find('b').text
            shift = tds[3].find('b').text.strip('\n')

            # Add the card's information to the list
            card_data.append({
                'name': name,
                'collector_info': collector_info,
                'set': set,
                'rarity': rarity,
                'price': price,
                'shift': shift
            })

    # Return the card data as JSON
    return jsonify(card_data)

@api.route('/shipping_japan_post', methods=['POST'])
def get_japanpost_shipping_price():
    data = request.json
    cards = data['cards']
    jp_zipcode = data['japanZip']
    us_zipcode = data['usZip']
    result = function_runner(japan_post, cards, jp_zipcode, us_zipcode)
    response = jsonify(result)
    return response

@api.route('/shipping_DHL', methods=['POST'])
def get_DHL_shipping_price():
    data = request.json
    cards = data['cards']
    jp_zipcode = data['japanZip']
    us_zipcode = data['usZip']
    result = function_runner(DHL, cards, jp_zipcode, us_zipcode)
    response = jsonify(result)
    return response

@api.route('/shipping_Fedex', methods=['POST'])
def get_Fedex_shipping_price():
    data = request.json
    cards = data['cards']
    jp_zipcode = data['japanZip']
    us_zipcode = data['usZip']
    result = function_runner(fedex, cards, jp_zipcode, us_zipcode)
    response = jsonify(result)
    return response

@api.route('/get_exchange_rate', methods=['POST'])
def get_exchange_rate_route():
    data = request.json
    base_currency = data['baseCurrency']
    target_currency = data['targetCurrency']

    rate = get_exchange_rate(base_currency, target_currency)

    if rate:
        response = jsonify(rate=rate)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        response = jsonify(error="Error fetching exchange rate")
        response.status_code = 500
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response