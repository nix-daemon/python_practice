print("Enter two numbers and I will give you their sum.")
a = input("Enter the first number: ")
b = input("Enter the second number: ")
try:
    sum = int(a) + int(b)
except ValueError:
    print("I can only add two integers together!")
else:
    print(sum)