filename = 'text_files/learning_python.txt'
c_line = []
with open(filename) as file_object:
    contents = file_object.read()
print(1)
print(contents)

print(2)
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

print(3)
with open(filename) as file_object:
    lines= file_object.readlines()
for line in lines:
    print(line.strip())

print(4)
for line in lines:
    c_line.append(line.replace('Python', 'C'))
for line in c_line:
    print(line.strip())