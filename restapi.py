import json
import requests

position = {"x":0,"y":0,"z":0}

response = requests.get('http://localhost:8000/web/test.json')

d_resp = response.json()

#position should be empty
print(position)

#Printing & assigning json dictionary variables to LOCAL position variable
print("pos x:", d_resp["x"]) 
position["x"] = d_resp["x"]

print("pos y:", d_resp["y"]) 
position["y"] = d_resp["y"]

print("pos z:", d_resp["z"]) 
position["z"] = d_resp["z"]

print(position)