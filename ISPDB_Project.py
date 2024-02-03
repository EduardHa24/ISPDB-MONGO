from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.ISPDB
col = db.Devices

Device_Name = input("Enter name here: ")
Device_Ver = input("Enter Version: ")
Device_Model = input("Enter Model name: ")


if Device_Name == Device_Model:
        print("Device Already Exists")
else:
        col.insert_one({"name": Device_Name,
                        "model": Device_Model,
                        "version":Device_Ver,})

        print("Data Added")

for col in col.find():
    print(col)
