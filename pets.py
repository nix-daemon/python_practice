lelouch = {'name': 'lelouch', 'type': 'cat', 'owner': 'john'}
nunnally = {'name': 'nunnally', 'type': 'cat', 'owner': 'john'}

pets = [lelouch, nunnally]

for pet in pets:
	print(f"{pet['name'].title()} is a {pet['type']} owned by {pet['owner'].title()}")
	for key, value in pet.items():
		print(f"{key} : {value}")