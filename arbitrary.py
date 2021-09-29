# arbitrary number of arguments but don't know what kind of values will be passed - use ** to create empty dictionary to accept any number of key-value pairs
def profile(first, last, **user_info):
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = profile('Kim', 'Lee', age = 30, hobby = 'basketball')
print(user_profile)

#arbitary arguments with fixed items
def make_pizza(size, *toppings):
    print("\nHere is your pizza order:")
    print(f"\n{size.title()} size")
    print("Toppings -")

    for topping in toppings:
        print(f"\t{topping.title()}")

new_order = make_pizza('medium', 'mushrooms', 'extra cheese', 'sausages')


#practice
def sandwich_order(*toppings):
    print("\nHere is your sandwich order:")

    for topping in toppings:
        print(f"\t - {topping}")

cheesesteak = sandwich_order('cheesesteak', 'fries', 'cheddar')
tuna = sandwich_order('tuna salad', 'lettuce', 'tomatoes')
italian = sandwich_order('salami', 'ham', 'mustard')

#practice
def car_info(model, company, **info):
    info['Model'] = model
    info['Maker'] = company
    return info

my_car = car_info('Genesis', 'Hyundai', Year = 2019, Price = '50,000 USD')
print(my_car)
