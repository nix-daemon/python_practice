sandwich_orders = ['cuban', 'hero', 'chopped cheese']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"I finished making your {sandwich} sandwich!")
	finished_sandwiches.append(sandwich)
print("\nOrders")
for sandwich in finished_sandwiches:
	print(f"{sandwich.title()} order complete!")