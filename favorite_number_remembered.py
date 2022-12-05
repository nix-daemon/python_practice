import json, random

filename = 'json/number.json'

try:
    with open(filename) as f:
        num = json.load(f)
except FileNotFoundError:
    num = random.randint(0,10) # For Spyder, since Spyder can't call input()
#    num = int(input("Please enter your favorite number: "))
    with open(filename, 'w') as f:
        json.dump(num, f)
else:
    print(f"I know your favorite number! It's {num}")