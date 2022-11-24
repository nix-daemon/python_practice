current_users = ['Admin', 'psmith', 'Jrutherford', 'dmoore', 'srutherford']
new_users = ['helpdesk', 'dmoore', 'jrutherford', 'jsilverhand', 'mblackhand']
current_users_lower = []
for current_user in current_users:
	current_users_lower.append(current_user.lower())

for new_user in new_users:
	if new_user in current_users_lower:
		print(f"{new_user.title()} already exists! Please enter a new username.")
	else:
		print(f"{new_user.title()} is available!")