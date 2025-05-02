import requests
import pymongo
from pymongo import MongoClient
db_url='mongodb://localhost:27017/'
try:
    client=MongoClient(db_url)
    db=client['11am']
    emp_col=db['pacchu']
    emp_col.insert_one[