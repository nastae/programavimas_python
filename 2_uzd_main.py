import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['restaurants_db']
collection_restaurant = db['restaurant']

print("1. Parašykite užklausą atvaizduojančią visus dokumentus iš restoranų rinkinio")
for x in collection_restaurant.find():
    print(x)

print("2. Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine - visiems dokumentams")
for x in collection_restaurant.find({}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1}):
    print(x)

print("3. Parašykite užklausą, kuri ayvaizduotų laukus - restaurant_id, name, borough ir cuisine -, bet nerodytų lauko field_id visiems dokumentams")
for x in collection_restaurant.retaurants.find({}, {"_id": 0, 'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1}):
    print(x)

print("4. Parašykite užklausą, kuri parodytų visus miestelio Bronx restoranus")
for x in collection_restaurant.find({"borough": "Bronx"}):
    print(x)

print("5. Parašykite užklausą, kuri parodytų restoranus su įvertinimu tarp 80 ir 100.")
for x in collection_restaurant.find({'grades': {'$elemMatch': {'score': {'$gte': 80, '$lte': 100 }}}}):
    print(x)