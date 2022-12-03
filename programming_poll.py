filename = 'text_files/programming_poll.txt'

with open(filename, 'a') as file_object:
    while 1 == 1:
        reason = input("Please enter why you like programming: ")
        print("Your response has been logged")
        file_object.write(f"{reason}\n")