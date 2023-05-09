from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://admin:admin@cluster0.wj4vxhv.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), ssl=True)
db = client["pokemon_cards"]
collection = db["cards"]
collection.create_index([("US_name", "text")])
# Send a ping to confirm a successful connection
print("Trying to connect to MongoDB")
try:
    print("Trying to Ping Server")
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)