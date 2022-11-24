guests = ['markiplier', 'mr. beast', 'matpat']
print(f"{guests[0].title()}, would you like to come to dinner?")
print(f"{guests[1].title()}, would you like to come to dinner?")
print(f"{guests[2].title()}, would you like to come to dinner?")

print(f"\n{guests.pop(1).title()} can't make it!")
guests.insert(1, 'jaden')
print(f"\n{guests[0].title()}, would you like to come to dinner?")
print(f"{guests[1].title()}, would you like to come to dinner?")
print(f"{guests[2].title()}, would you like to come to dinner?")