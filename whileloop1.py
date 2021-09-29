sandwich_orders = ['ham and cheese', 'tuna mayo', 'egg salad', 'italian', 'philly cheesesteak']
finished_sandwiches = []

while len(sandwich_orders) != 0:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print(finished_sandwiches)

#exercise 2
sandwich_orders = ['ham and cheese', 'tuna mayo', 'egg salad', 'italian', 'philly cheesesteak', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    if sandwich == 'pastrami':
        print("Sorry, we are out of pastrami.")
    else:
        print(f"I made your {sandwich} sandwich.")
        finished_sandwiches.append(sandwich)

print("\nComplete Order List")
print(finished_sandwiches)

print(sandwich_orders)

#exercise 3
responses = {}

polling_active = True
while polling_active:
    name = input("What is your name? ")
    response = input("If you could visit one place in world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to exit (yes/no)? ")
    if repeat == 'yes':
        polling_active = False

print(responses)