class Restaurant:
	"""A simple attempt to model a restaurant"""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"This restaurant is named {self.restaurant_name}. They serve "
			f"{self.cuisine_type}!")

	def open_restuarant(self):
		print(f"{self.restaurant_name} is now open!!")

	def set_number_served(self, number_served):
		"""Set the number served to a given value"""
		self.number_served = number_served

	def increment_number_served(self, served):
		"""Increment the number served by the given value"""
		if served > 0:
			self.number_served += served
		else:
			print("You can't rollback number served!")

restaurant_1 = Restaurant('Subway', 'Subs')
restaurant_2 = Restaurant('Takosushi', 'Sushi')
restaurant_3 = Restaurant('Mellow Mushroom', 'Pizza')

print(restaurant_1.number_served)

restaurant_1.number_served = 30
print(restaurant_1.number_served)

restaurant_1.set_number_served(60)
print(restaurant_1.number_served)

restaurant_1.increment_number_served(100)
print(restaurant_1.number_served)