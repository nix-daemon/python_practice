class User:
	"""A simple attempt to model a user."""

	def __init__(self, first_name, last_name, account_name, sid):
		self.first_name = first_name
		self.last_name = last_name
		self.account_name = account_name
		self.sid = sid

	def describe_user(self):
		"""Return information about a user."""
		print("\nUser Info:")
		print(f"First Name: {self.first_name}")
		print(f"Last Name: {self.last_name}")
		print(f"Username: {self.account_name}")
		print(f"User SID: {self.sid}")

	def greet_user(self):
		print(f"Welcome back {self.first_name} {self.last_name}!")

user_1 = User('Johnathan', 'Rutherford', 'jmruthe', 0)
user_2 = User('Sharaya', 'Rutherford', 'ssruthe', 1)
user_3 = User('Zara', 'Rutherford', 'zaruthe', 2)

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()