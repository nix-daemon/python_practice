prompt = "Please enter the toppings you would like on your pizza: "
prompt += "(Enter quit to exit the program)"

active = True
while active == True:
	topping = input(prompt)
	if topping == 'quit':
		active = False
	else:
		print(f"Adding {topping} to pizza!")