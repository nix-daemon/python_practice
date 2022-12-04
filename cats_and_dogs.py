filenames = ['cats.txt', 'text_files/dogs.txt']

for filename in filenames:
    try:
        with open(filename, 'r') as f:
            contents = f.readlines()
    except FileNotFoundError:
        print(f"The file {filename} does not exit")
    else:
        for line in contents:
            print(line)