from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.ISPDB
collection = db.Devices

Device_Name = input("Enter name here: ")
Device_Ver = input("Enter Version: ")
Device_Model = input("Enter Model name: ")

for col in collection.find({'name':Device_Name}):
    if col != Device_Name:
        print("Device already exists")
    else:
        collection.insert_one({"name": Device_Name,
                                "model": Device_Model,
                                "version":Device_Ver,})
        print("Device added")
    continue

for x in collection.find():
     print(x)