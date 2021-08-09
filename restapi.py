import json
import requests

PATH = 'http://localhost:8000/web/test.json'


position = {"x":0,"y":0,"z":0}

print("Connecting to ",PATH)
response = requests.get(PATH)

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

input(("Any key to exit..."))