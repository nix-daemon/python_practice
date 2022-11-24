python_dictionary = {
	'print': 'prints the specified data',
	'.title()': 'capitalizes the first letter of the specified word',
	'len()': 'returns the number of items in a set of data',
	'for': 'used to execute a command for each item in a group',
	'if': 'used to start a conditional statement',
	'.items()': 'retrieves key value pairs from a dictionary',
	'set()': 'creates a set, which combines the same values in a dictionary',
	'sorted()': 'sorts a list alphabetically',
	'.values()': 'retrieves values from key value pairs',
	'range()': 'creates a list of numbers in order'
}
for word, definition in python_dictionary.items():
	print(f"{word}: {definition}")