person_0 = {'first_name': 'johnny', 'last_name': 'silverhand', 'age': 89, 'city': 'night city'}
person_1 = {'first_name': 'morgan', 'last_name': 'blackhand', 'age': 101, 'city': 'night city'}
person_2 = {'first_name': 'john', 'last_name': 'rutherford', 'age': 33, 'city': 'augusta'}

people = [person_0, person_1, person_2]
for person in people:
	print(f"\nName:{person['first_name']}\nLast Name:{person['last_name']}" 
		f" age:{person['age']} city:{person['city']}")