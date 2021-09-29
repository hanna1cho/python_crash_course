prompt = ("\nPlease state your message")
prompt += "\n(or enter 'quit' to move on.): "

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

#using a flag
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#using break to exit a loop
prompt = ("\nPlease enter food you'd like to order")
prompt += "\n(or enter 'quit' to end program.): "

while True:
    food = input(prompt)

    if food == 'quit':
        break
    else: 
        print (f"We will have your {food.upper()} ready in the next 15 minutes")