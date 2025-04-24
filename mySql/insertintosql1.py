import requests, mysql.connector
data=requests.get('https://dummyjson.com/products')
product_data=data.json()
status_code=data.status_code
print(product_data)
print(status_code)

products=product_data['products']
print(len(products))

new_products=[]
for product in products:
    new_products.append((product['id'],product['title'],product['price'],product['category']))
    print(new_products)

dbcon=None
try:
    dbcon=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='11am'
    )
    cursor=dbcon.cursor()
    sql_st='''insert into product values(%s,%s,%s,%s),'''
    cursor.executemany(sql_st,new_products)
    dbcon.commit()
    print("Products data write into product table")
except mysql.connector.DatabaseError as err:
    print(err)
finally:
    pass
            
