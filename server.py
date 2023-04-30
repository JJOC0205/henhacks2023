import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from canvas_api import *
from main import api_key
uri = "mongodb+srv://jjoc0205:Jmwins00@henhacksdb.bzkmaw2.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

mydb = client["HenHacks2023"]
mycol = mydb["user_data"]
doc = create_dict("Rachel",api_key[0])
x = mydb.insert(doc)
# cursor = mycol.find({})
# for document in cursor: 
#     print(document.values)