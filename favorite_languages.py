favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
	print(name.title())

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking our poll!")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

new_people = ['jen', 'sarah', 'john']

for name in new_people:
	if name in favorite_languages:
		print(f"{name.title()}, thank you for responding.")
	else:
		print(f"{name.title()}, please take our poll.")
