def make_shirt(size = 'Large', message = 'I Love Python'):
	"""Accept size and message to create and display a custom shirt"""
	print(f"Confirm that you would like a {size.title()} shirt printed with "
		f"the message {message}.")

make_shirt('small', 'Plus Ultra')
make_shirt(size = 'large', message = 'Plus Ultra')
make_shirt()
make_shirt('medium')
make_shirt('small', 'Twin Peaks')