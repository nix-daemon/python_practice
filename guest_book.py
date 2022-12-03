filename = 'text_files/guest_book.txt'

with open(filename, 'a') as file_object:
    while 1 == 1:
        name = input("Please enter your name: ")
        print(f"Thanks for stopping by {name}!")
        file_object.write(f"{name}\n")