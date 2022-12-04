import json

username = input("What is your name?")

filename = 'json/username.json'
with open (filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when yu come back, {username}!")