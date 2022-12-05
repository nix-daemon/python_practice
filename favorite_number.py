import json

num = int(input("Please enter your favorite number: ")
filename = 'json/number.json'

with open(filename, 'w') as f:
    json.dump(num, f)
