filename = 'guest.txt'

with open(filename, 'a') as file_object:
        file_object.write("Guest List:\n")


active = True
while active:
    name = input("Hello, what is your name? \n(Enter 'quit' to end the program)")
    
    if name == 'quit':
        active = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")
    



filename1 = 'guest_book.txt'

active = True
while active:
    name = input("Hello, what is your name? \n(Enter 'quit' to end the program)")

    if name == 'quit':
        active = False
    else:
        with open(filename1, 'a') as file_object:
            file_object.write(f"{name}\n")

