filenames = ['cats.txt', 'text_files/dogs.txt']

for filename in filenames:
    try:
        with open(filename, 'r') as f:
            contents = f.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in contents:
            print(line)