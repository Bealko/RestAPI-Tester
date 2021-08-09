import json
import requests

response = requests.get('http://localhost:8000/web/coords.json')

file = response.json()

#create dictionary
pairs = file.items()

for item,value in pairs:
    print (item,value)
