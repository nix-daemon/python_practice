favorite_places = {'john': ['italy', 'japan'], 'raya': ['japan'], 'chris': ['texas']}

for person, places in favorite_places.items():
	print(f"{person.title()}'s favorite places are:")
	for place in places:
		print(place)
	print("...")
