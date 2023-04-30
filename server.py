import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from canvas_api import *

def server(key:list):
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
    doc = create_dict(key)
    x = mycol.insert_one(doc)

def grab_database_values(key):
    uri = "mongodb+srv://jjoc0205:Jmwins00@henhacksdb.bzkmaw2.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    split_key = key.split(",")
    name = split_key[0]
    email = split_key[1]
    mydb = client["HenHacks2023"]
    mycol = mydb["user_data"]
    doc = create_dict(key)
    all_data = mycol.find()
    all_names = []
    my_courses = set(doc["courses"])
    for document in all_data:
        if my_courses.intersection(set(document["courses"])):
            my_courses.intersection_update(set(document["courses"]))
            all_names.append(document["name"] + ":" + document["ud-email"] + ":" + str(my_courses.intersection(set(document["courses"]))))
    # for document in all_data:
    #     if set(document["courses"]).intersection(my_courses):
    #         print(set(document["courses"]).intersection(my_courses))
    #         all_names.append(document["name"])
    print(all_names)
    return (all_names)
