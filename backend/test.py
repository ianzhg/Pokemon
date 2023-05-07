import requests

#Testing posting data
url = "http://127.0.0.1:5000/store_data"
data = {
    "unique_id": "S1234",
    "JP_name": "ポケモンカード",
    "JP_price": 1000,
    "US_name": "Pokemon Card",
    "US_price": 10
}
response = requests.post(url, json=data)
print(response.json())

#Testing getting data
response = requests.get(url +'/S1234')
print(response.json())


#Testing updating data
data = {
    "JP_price": 1200,
    "US_name": "Pokemon Trading Card"
}
response = requests.put(url + "/update_data/S1234", json=data)

data = {
    "JP_name": "Miao Wa",
    "US_price": -10000
}
response = requests.put(url + "/update_data/S1234", json=data)

data = {
    "JP_name": "JJ",
    "US_price": -1,
    "US_name": "USA!!",
    "JP_price": -2
}
response = requests.put(url + "/update_data/S1234", json=data)
