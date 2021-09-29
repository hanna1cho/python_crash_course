# filename = 'cats.txt'

# with open(filename, 'w') as cats:
#     cats.write("Jerry\n")
#     cats.write("Mimi\n")
#     cats.write("Russ\n")

# filename1 = 'dogs.txt'

# with open(filename1, 'w') as dogs:
#     dogs.write("Coco\n")
#     dogs.write("Apple\n")
#     dogs.write("Blue\n")

filenames = ['dogs.txt', 'rabbits.txt', 'cats.txt']
for filename in filenames:
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except: 
            pass


line = "Row, row, row your boat"
line.count('row')

line.lower().count('row')