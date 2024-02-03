from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.ISPDB
collection = db.Devices

Device_Name = input("Enter name here: ").strip()
Device_Ver = input("Enter Version: ").strip()
Device_Model = input("Enter Model name: ").strip()

exists = collection.count_documents({'name':Device_Name})

if exists > 0:
    print("Device already exists")
else:
    collection.insert_one({"name": Device_Name,
                            "model": Device_Model,
                            "version":Device_Ver,})
    print("Device added")

for x in collection.find():
     print(x)