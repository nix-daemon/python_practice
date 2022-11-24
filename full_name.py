#nix-daemon 15Nov22
#Assigns a first name and last name, then prints the name and message in a few different format strings
first_name = 'johnny'
last_name = 'silverhand'
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)