import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.json())  # Response as JSON