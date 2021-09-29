# prompt = "Enter your age: "
# active = True
# while active:
#     age = input(prompt)

#     if str(age) =='quit':
#         break
#     elif int(age) > 15:
#         print("Ticket is $15.")
#     elif int(age) >= 3:
#         print("Ticket is $10.")
#     elif int(age) < 3:
#         print("Ticket is free.")


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


#Creating dictionary with user input
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which national park would you like to visit? ")

    # create dictionary key and value
    responses[name] = response

    repeat = input("Would you like to exit the poll? ")
    if repeat == 'yes':
        polling_active = False

print("\n----Poll Results---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response}.")

    

