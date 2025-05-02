from pymongo import MongoClient
db_url='mongodb://localhost:27017/'
try:
    client=MongoClient(db_url) 
    db=client['pacchu']
    emp_col=db['myCollection']
    emp_col.insert_one({"eid":101,"ename":"Rahul","esal":45000.45})
    print("New Employee Doc inserted successfully")

    # Without variable de-structure way(just for me)
    # MongoClient('mongodb://localhost:27017/')['pacchu']['myCollecton'].insert_one({"eid":101,"ename":"Rahul","esal":45000.45})
    # print("Data Inserted Successfully!!!")

except Exception as err:
    print(err)





