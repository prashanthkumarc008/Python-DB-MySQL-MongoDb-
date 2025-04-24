import json,requests
products=requests.get('https://dummyjson.com/products').json()['products']
# print(type(products)) list

fp=None
try:
    fp=open('product.json','w')
    json.dump(products,fp)
    print("New JSON File created successfully")
except Exception as err:
    print(err)
finally:
    fp.close()
