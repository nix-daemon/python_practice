def show_messages(unsent, sent):
	while unsent:
		current_msg = unsent.pop()
		print(f"Sending message: {current_msg}")
		sent.append(current_msg)
	print("\nList of sent messages: ")

unsent = ["hi", "how have you been", "what's for dinner"]
sent = []
show_messages(unsent[:], sent)
for message in sent:
	print(message)
print(sent)
print(unsent)