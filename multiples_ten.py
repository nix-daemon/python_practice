number = input("Enter a number, and I will tell you if it is a multiple of 10"
				" or not: ")
number = int(number)

if number % 10 == 0:
	print(f"The number {number} is a multiple of 10!")
else:
	print(f"The number {number} is not a multiple of 10!")