#invoke Products Rest API and 
# insert data into mongoDB Collection
import requests, pymongo
products=requests.get('https://dummyjson.com/products').json()['products']
print(type(products))
print(len(products))