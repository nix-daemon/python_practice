filenames = ['text_files/frankenstein.txt', 'text_files/metamorphosis.txt']

for filename in filenames:
    with open(filename, encoding = 'utf-8') as f:
        contents = f.read()
    num_of_fear = contents.lower().count('the ')
    print(num_of_fear)