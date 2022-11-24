sandwich_orders = ['cuban', 'pastrami', 'hero', 'pastrami', 'chopped cheese', 'pastrami']
finished_sandwiches = []
print("Terribly sorry, but the deli has run out of Pastrami!")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"I finished making your {sandwich} sandwich!")
	finished_sandwiches.append(sandwich)
print("\nOrders")
for sandwich in finished_sandwiches:
	print(f"{sandwich.title()} order complete!")