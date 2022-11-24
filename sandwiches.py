def make_sandwich(*ingredients):
    print("\nMaking your sandwich with:")
    for ingredient in ingredients:
        print(f"- {ingredient.title()}")

make_sandwich('ham', 'cheese')
make_sandwich('pepperoni')
make_sandwich('turkey', 'cheese', 'lettuce', 'tomato', 'mayo', 'red onions')