#defining function
def greet_user():
    """display a simple greeting"""
    print('Hello!')

greet_user()

#passing information to a function
def greet_user(username):
    """display a simple greeting"""
    print(f'Hello, {username.title()}!')

greet_user('hanna')
greet_user('sarah')

def display_message():
    print("I am learning about 'functions' in chapter 8.")

display_message()

def favorite_book(book):
    print(f"{book.title()} is my favorite book.")

favorite_book('harry potter')

#positional arguments
def describe_pet(animal_type, pet_name):
    """display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'zoey')
describe_pet('cat', 'meow')

#keyword arguments
describe_pet(animal_type='giraffe', pet_name='bob')
describe_pet(pet_name='mimi', animal_type='hamster')

#default values - default values MUST COME AFTER all undefined parameters are listed
def describe_pet(pet_name, animal_type='dog'):
    """display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='Minnie')
describe_pet('Willie')
describe_pet(pet_name='Harry', animal_type='goldfish')