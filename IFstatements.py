alien_color = "yellow"
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == "yellow":
    print("You earned 1 point")

alien_color = "purple"
if alien_color == 'green':
    print("You earned 5 points.")
else:
    print("You earned 10 points.")

alien_color = "red"
if alien_color == 'green':
    print("You earned 5 points.")
elif alien_color == "yellow":
    print("You earned 10 point")
else:
    print("You earned 15 points")


print("\n")
age = 78
if age < 2:
    print ("Jason is a baby")
elif age < 4:
    print ("Jason is a toddler")
elif age < 13:
    print ("Jason is a kid")
elif age < 20:
    print ("Jason is a teenager")
elif age < 65:
    print ("Jason is an adult")
else: 
    print ("Jason is an elder")

print("\n")
favorite_fruits = ["strawberry", "kiwi", "cherry"]
if "banana" in favorite_fruits:
    print ("Hanna loves bananas")
if "strawberry" in favorite_fruits:
    print ("Hanna loves strawberries")
if "kiwi" in favorite_fruits:
    print ("Hanna loves strawberries")
if "apple" in favorite_fruits:
    print ("Hanna loves apples")
if "cherry" in favorite_fruits:
    print ("Hanna loves cherries")

#combining for loops in if statements
print("\n")
pizza_toppings = ['extra cheese', 'mushrooms', 'sausages']
for topping in pizza_toppings:
    if topping == "mushrooms":
        print ("Sorry, we are out of mushrooms")
    else: 
        print (f"Adding {topping}")

print ("Finshished making your pizza!")


#checking that a list is not empty starts with an if statement
print("\n")
requested_toppings = ["extra cheese", "green peppers"]
if requested_toppings:
    for topping in requested_toppings:
        print (f"Adding {topping}")
    print ("Finished making your pizza!")
else: 
    print ("Are you sure you want a plain pizza")

requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print (f"Adding {topping}")
    print ("Finished making your pizza!")
else: 
    print ("\nAre you sure you want a plain pizza?")