filename = 'learning_python.txt'

#print entire contents by reading file
with open(filename) as file_object:
    contents = file_object.read()

print(contents)

#print by looping over the file
with open(filename) as file_object:
    for line in file_object:
        print(line)

#print by storing the lines in a list
with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)

for line in lines:
    print(line.rstrip())


# #replace a word in the string
with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    line = line.replace('Python', 'javascript')
    print(line)