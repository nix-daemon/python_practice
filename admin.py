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

class Admin(User):
    "Models admin, a type of user"
    def __init__(self, first_name, last_name, account_name,sid):
        super().__init__(first_name,last_name, account_name, sid)
        self.privileges = "can delete post", "can add post", "can ban user"

    def show_privileges(self):
        print(f"As an admin you have the following privileges:")
        for privilege in self.privileges:
            print(privilege)

admin_1 = Admin('John', 'Rutherford', 'jmruthe.sa', 100)
admin_1.show_privileges()