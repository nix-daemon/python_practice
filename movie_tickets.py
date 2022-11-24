prompt = "Welcome to the movies! How old are you?"
prompt += "(Enter 'quit to exit!')"
active = True

while active == True:
	age = input(prompt)
	if age == 'quit':
		active = False
	else:
		age = int(age)
		if age < 3:
			print("Your ticket is free!")
		elif age >= 3 and age <= 12:
			print("Your ticket will be $10.")
		elif age > 12:
			print("Your ticket will be $15.")