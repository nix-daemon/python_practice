unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
	"""Simulate printign each design, until none are left.
	Move each design to completed_models afte printing.
	"""
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""
print("\n The following models have been printed:")
for completed_model in completed_models:
	print(completed_model)