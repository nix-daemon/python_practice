class Restaurant:
	"""A simple attempt to model a restaurant"""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"This restaurant is named {self.restaurant_name}. They serve "
			f"{self.cuisine_type}!")

	def open_restuarant(self):
		print(f"{self.restaurant_name} is now open!!")

restaurant_1 = Restaurant('Subway', 'Subs')
restaurant_2 = Restaurant('Takosushi', 'Sushi')
restaurant_3 = Restaurant('Mellow Mushroom', 'Pizza')
#restaurants = [restaurant_1, restaurant_2, restaurant_3]

print(restaurant_1.restaurant_name)
print(restaurant_1.cuisine_type)
restaurant_1.describe_restaurant()
restaurant_1.open_restuarant()
print("\n")
print(restaurant_2.restaurant_name)
print(restaurant_2.cuisine_type)
restaurant_2.describe_restaurant()
restaurant_2.open_restuarant()
print("\n")
print(restaurant_3.restaurant_name)
print(restaurant_3.cuisine_type)
restaurant_3.describe_restaurant()
restaurant_3.open_restuarant()

#for restaurant in restaurants:
#	print(restaurant.restaurant_name)
#	print(restaurant.cuisine_type)
#	restaurant.describe_restaurant()
#	restaurant.open_restuarant()
#	print("\n")