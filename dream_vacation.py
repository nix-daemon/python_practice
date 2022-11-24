responses = {}
print("We are taking a poll of users to find out their dream vacations.")

repeat = 'yes'

while repeat == 'yes':
	name = input("What is your name?")
	destination = input("Where would you like to go?")
	responses[name] = destination
	repeat = input("Would you like to allow another person to enter their "
		"response? (yes/no)")
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name.title()} would like to travel to {response.title()}")