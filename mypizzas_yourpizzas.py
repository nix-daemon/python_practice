my_pizzas = ["pepperoni", "supreme", "meat lovers"]
your_pizzas = my_pizzas[:]

my_pizzas.append("hawaiian")
your_pizzas.append("anchovi")

print("My favorite pizzas are:")
for pizza in my_pizzas:
	print(pizza)

print("My friend's favorite pizzas are:")
for pizza in your_pizzas:
	print(pizza)