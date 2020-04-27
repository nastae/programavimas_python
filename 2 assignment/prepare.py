import pymongo
from bson.json_util import loads

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['restaurants_db']
collection_restaurant = db['restaurant']

with open('restaurants.json') as f:
    file_data = loads(f.read())

collection_restaurant.insert_many(file_data)

client.close()