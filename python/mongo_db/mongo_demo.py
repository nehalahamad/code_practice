from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["latest_db"]
collection = db["students"]

results = collection.find({})
for result in results:
    print(result)

    