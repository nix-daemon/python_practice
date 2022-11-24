guests = ['markiplier', 'mr. beast', 'matpat']
print(f"{guests[0].title()}, would you like to come to dinner?")
print(f"{guests[1].title()}, would you like to come to dinner?")
print(f"{guests[2].title()}, would you like to come to dinner?")

print(f"\n{guests.pop(1).title()} can't make it!")
guests.insert(1, 'jaden')
print(f"\n{guests[0].title()}, would you like to come to dinner?")
print(f"{guests[1].title()}, would you like to come to dinner?")
print(f"{guests[2].title()}, would you like to come to dinner?")

print("\nWe found a bigger table!")

guests.insert(0, 'cash jordon')
print(guests)
print("\n")

guests.insert(2, 'david tennant')
print(guests)
print("\n")

guests.append('PBG')
print(guests)
print("\n")

print(f"\n{guests[0].title()}, would you like to come to dinner?")
print(f"{guests[1].title()}, would you like to come to dinner?")
print(f"{guests[2].title()}, would you like to come to dinner?")
print(f"{guests[3].title()}, would you like to come to dinner?")
print(f"{guests[4].title()}, would you like to come to dinner?")
print(f"{guests[5].title()}, would you like to come to dinner?")