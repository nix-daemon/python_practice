def describe_pet(pet_name, animal_type = 'cat'):
	"""Display information about a pet"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}!")

describe_pet('cat', 'lelouch')
describe_pet('cat', 'nunnally')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(pet_name = 'xena')