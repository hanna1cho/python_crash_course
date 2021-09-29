#Returning a dictionary
def person(first_name, last_name, age=None):
    data = {'first' : first_name, 'last' : last_name}
    if age:
        data['age'] = age
    return data

journalist = person('Oprah', 'Winfrey', 55)
singer = person('Selena', 'Gomex', 30)
print(journalist)
print(singer)

#Using function with a while loop
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name. \nEnter 'q' at any time to quit.")
    
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
