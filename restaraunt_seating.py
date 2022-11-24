dinner_group = input("How many people are in your dinner group? ")
dinner_group = int(dinner_group)

if dinner_group > 8:
	print("Please wait until the next table opens up.")
else:
	print("Your table is ready!")