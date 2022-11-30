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

class Icecreamstand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """Represents aspects of an ice cream stand which is a type of 
        restaurant"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = 'chocolate', 'strawberry', 'rocky road'

    def list_flavors(self):
        "Prints a list of flavors for the ice cream stand."
        print(f"Welcome to {self.restaurant_name}! We have the following "
        "flavors:")
        for flavor in self.flavors:
            print(flavor.title())

my_ice_cream_stand = Icecreamstand('Marble Slab', 'Ice Cream')
my_ice_cream_stand.open_restuarant()
my_ice_cream_stand.list_flavors()

