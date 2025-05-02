import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['pacchu']

mycol = mydb["myCollection"]

print(mydb.list_collection_names())
