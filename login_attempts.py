class User:
	"""A simple attempt to model a user."""

	def __init__(self, first_name, last_name, account_name, sid):
		self.first_name = first_name
		self.last_name = last_name
		self.account_name = account_name
		self.sid = sid
		self.login_attempts = 0

	def describe_user(self):
		"""Return information about a user."""
		print("\nUser Info:")
		print(f"First Name: {self.first_name}")
		print(f"Last Name: {self.last_name}")
		print(f"Username: {self.account_name}")
		print(f"User SID: {self.sid}")

	def greet_user(self):
		print(f"Welcome back {self.first_name} {self.last_name}!")

	def increment_login_attempts(self):
		"""Increment the number of login attempts by 1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset login attempts to 0"""
		self.login_attempts = 0

user_1 = User('Johnathan', 'Rutherford', 'jmruthe', 0)
user_2 = User('Sharaya', 'Rutherford', 'ssruthe', 1)
user_3 = User('Zara', 'Rutherford', 'zaruthe', 2)

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)