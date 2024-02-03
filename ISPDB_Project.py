from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.ISPDB
col = db.Devices

Device_Name = input("Enter name here: ")
Device_Ver = input("Enter Version: ")
Device_Model = input("Enter Model name: ")


def insert_data(Device_Name,Device_Ver,Device_Model):
    if Device_Name == Device_Name:
        print("Device Already Exists")
    else:
        col.insert_one({"name": Device_Name,
                        "model": Device_Model,
                        "version":Device_Ver,})

        print("Data Added")
    return insert_data(Device_Name,Device_Ver,Device_Model)



    


for col in col.find():
    print(col)
