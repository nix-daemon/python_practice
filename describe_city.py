def describe_city(city, country = 'United States'):
	"""Displays a sentence about the city and country you enter"""
	print(f"{city.title()} is located in {country.title()}.")

describe_city('fort worth')
describe_city('augusta')
describe_city('tokyo')