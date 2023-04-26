import requests
import re
import time
import datetime
from bs4 import BeautifulSoup

cardrush_url = "https://www.cardrush-pokemon.jp/phone/new"
#TODO: Change this when backend is published
db_url = "http://127.0.0.1:5000"
url = f"{cardrush_url}/new?page=1"


#Extrating goods and prices given the beautiful soup content
def extract_goods_and_prices(soup):
    results = {}

    item_data_divs = soup.find_all('div', class_='item_data')

    for div in item_data_divs:
        goods_name = div.find('span', class_='goods_name')
        selling_price = div.find('p', class_='selling_price')
        model_number = div.find('span', class_ ='model_number')

        if goods_name and selling_price:
            #Extracting name of the card
            goods_name_text = goods_name.text.strip()
            #Extracting ID of the card
            match = re.search(r'\{(\d+/\d+)\}', goods_name_text)
            if match:
                goods_id = match.group(1)
                encoded_goods_id = goods_id.replace('/', '>')
                
                #Extracting the price of the card
                selling_price_text = selling_price.text.strip()
                price = int(re.sub(r'\D+', '', selling_price_text))
                
                #Extracting the model of the card
                model_number_text = model_number.text.strip()
                model_value = re.search(r'S([^]]+)\]', model_number_text)

                if model_value:
                    model_number = 'S' + model_value.group(1)
                    result = {
                        'unique_id': model_number + '-' + encoded_goods_id,
                        'JP_name': goods_name_text,
                        'JP_price': price,
                        'US_price': -1,
                        'US_name': ''
                    }
                    results[result['unique_id']] = result

    return results

#Fetch and parse the given url
def fetch_and_parse(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print(f"Failed to fetch the page, status code: {response.status_code}")
        return None

#Reading for the first time
print("Reading Japanese Pokemon Card Info for the first time...")
# Fetch the first page
soup = fetch_and_parse(url)

if soup:
    # Extract goods_name and selling_price from the first page
    all_results = extract_goods_and_prices(soup)
    # Find the last page number
    pagebottom_div = soup.find('div', id='pagerbottom')

    if pagebottom_div:
        last_page_link = pagebottom_div.find_all('a', class_='pager_btn')[-2]
        last_page_number = int(last_page_link['href'].split('=')[-1])
        
        
        # Loop through the remaining pages
        for page_number in range(2, last_page_number + 1):
            print("Reading page " + str(page_number))
            page_url = f"{cardrush_url}/new?page={page_number}"
            soup = fetch_and_parse(page_url)

            if soup:
                # Extract goods_name and selling_price from the current page
                results = extract_goods_and_prices(soup)
                all_results.update(results)
                
    print("Total cards on cardcrush: " + len(all_results))
    #Pushing the data into the database
    for result in all_results.values():
        data = {
            "unique_id": result['unique_id'],
            "JP_name": result['JP_name'],
            "JP_price": result['JP_price'],
            "US_name": result['US_name'],
            "US_price": result['US_price']
        }
        response = requests.post(db_url+ "/store_data", json=data)
        print(response.json())
        print("\n")
    
print("Finished reading Japanese Pokemon Card Info")


#Updating the cards everything certain time
#TODO: Update me when deploying the app
time_interval = 1 * 60 #Time interval is now set to 1 minutes

while True:
    print("Updating Japanese cards in the database")
    soup = fetch_and_parse(url)
    
    if soup:
        # Extract goods_name and selling_price from the first page
        all_results = extract_goods_and_prices(soup)
        # Find the last page number
        pagebottom_div = soup.find('div', id='pagerbottom')

        if pagebottom_div:
            last_page_link = pagebottom_div.find_all('a', class_='pager_btn')[-2]
            last_page_number = int(last_page_link['href'].split('=')[-1])
            
            
            # Loop through the remaining pages
            for page_number in range(2, last_page_number + 1):
                print("Reading page " + str(page_number))
                page_url = f"{cardrush_url}/new?page={page_number}"
                soup = fetch_and_parse(page_url)

                if soup:
                    # Extract goods_name and selling_price from the current page
                    results = extract_goods_and_prices(soup)
                    all_results.update(results)
                
    print("Total cards on cardcrush: " + len(all_results))
    
    #Check if the Japanese price and name is different from the card in database and update accordingly
    for result in all_results.values():
        get_response = requests.get(db_url + '/get_data/' + result['unique_id'])
        
        #If the card is found in database, check if there is any different information
        if "output" in get_response.json().keys():
            current_card = get_response.json().get("output")
            different_info = {}
            if current_card['JP_name'] != result['JP_name']:
                different_info["JP_name"] = result['JP_name']
            if current_card['JP_price'] != result['JP_price']:
                different_info["JP_price"] = result['JP_price']    
            
            #Update the Japanese price and name if there is a change
            if different_info:
                update_response = requests.post(db_url+ "/update_data/" + result['unique_id'], json=different_info)
                print(update_response.json())
                print("\n")
            else:
                print("id: " + result['unique_id'] + ", " + result['JP_name'] + " is up-to-date!")
        #If the card is not fonud in database, add the card into database
        else:
            print("Found a new card! Storing in database now")
            data = {
                "unique_id": result['unique_id'],
                "JP_name": result['JP_name'],
                "JP_price": result['JP_price'],
                "US_name": result['US_name'],
                "US_price": result['US_price']
            }
            store_response = requests.post(db_url+ "/store_data", json=data)
            print(store_response.json())
            print("\n")
    

    print("Finished updating Japanese Pokemon Card Info")
    print("Next update is in " + str(datetime.timedelta(seconds=time_interval)) + " (hours/minutes/seconds)")

    time.sleep(time_interval)




