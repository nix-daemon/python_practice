import json

filename = 'json/number.json'

with open(filename) as f:
    num = json.load(f)
print(f"I know your favorite number! It's {num}!")