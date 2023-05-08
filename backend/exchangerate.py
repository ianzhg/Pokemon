import requests
def get_exchange_rate(base_currency, target_currency):
    url = f"http://www.floatrates.com/daily/{base_currency.lower()}.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        exchange_rate = data[target_currency.lower()]["rate"]
        return exchange_rate
    except requests.exceptions.HTTPError as e:
        print(f"Error getting exchange rate: {e}")
        return None

