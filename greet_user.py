import json 
filename = 'json/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back {username}!")