#tuples are immutable (not changeable)
dimensions = (100, 300)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

#rewriting the values 
dimensions = (40, 25)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#try it yourself
BuffetOptions = ("noodle soup", "dumplings", "egg salad", "seared tuna", "lobster")
print("\nBuffet Menu:")
for buffet in BuffetOptions:
    print(buffet.title())

# BuffetOptions[0] = "apple pie" this option does not work given tuples are immutable 

BuffetOptions = ("applie pie", "dumplings", "egg salad", "steak", "lobster")
print("\nBuffet Menu:")
for buffet in BuffetOptions:
    print(buffet.title())
