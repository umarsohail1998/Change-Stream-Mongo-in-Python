import os
import pymongo
from bson.json_util import dumps
url  ="mongodb+srv://umar:1234@umar.o7asv.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)

print("--- Server Started ---")
change_stream = client.changestream.collection.watch()
for change in change_stream:
    print(dumps(change))
    print('') # for readability only



# import pymongo
# import json
# url  ="mongodb+srv://umar:1234@umar.o7asv.mongodb.net/test?retryWrites=true&w=majority"
# myclient = pymongo.MongoClient(url)
# # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# # myclient.list_database_names()
# # print(myclient.list_database_names())
# mydb = myclient["test"]
# print(mydb.list_collection_names())
# with mydb.collection.watch() as stream:
#        for change in stream:
#            print(change)