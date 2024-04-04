from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json

uri = "mongodb+srv://longcule:Longcule1311@dic-db.szexbjy.mongodb.net/?retryWrites=true&w=majority&appName=dic-db"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Select the database
db = client['db-dic']

# Select the collection
collection = db['product']

# Retrieve all documents from the collection
documents = collection.find()

# Custom JSON encoder class to handle ObjectId serialization
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, object):
            return str(o)
        return super().default(o)

# Export documents to a JSON file using the custom encoder
with open('product2.json', 'w', encoding='utf-8') as file:
    json.dump(list(documents), file, cls=CustomJSONEncoder)