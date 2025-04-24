import requests

data = requests.get('https://jsonplaceholder.typicode.com/users')
users=data.json()
print(type(data))
print(type(data.json()))