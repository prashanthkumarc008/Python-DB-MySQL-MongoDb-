from pymongo import MongoClient

try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['pacchu']
    prod_col=db['myCollection']
    
    products=prod_col.find({})

    for product in products:
        print(product)

except Exception as err:
    print(err)