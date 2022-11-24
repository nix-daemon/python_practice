users = ['admin', 'psmith', 'jrutherford', 'dmoore', 'srutherford']

for user in users:
	if user == 'admin':
		print(f"Hello {user.title()}, would you like a status report?")
	else:
		print(f"Hello {user.title()}, thank you for logging in again.")