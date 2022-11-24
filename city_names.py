def city_country(city, country):
	city_countries = f"{city.title()}, {country.title()}"
	return city_countries

city = input("Please enter a city: ")
country = input("Please enter a country: ")
location = city_country(city, country)
print(location)