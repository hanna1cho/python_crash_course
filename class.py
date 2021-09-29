

class Dog:
    """A simple attempt to model a dog"""

# function that is part of a class is a method

# __init__ method is a special method that python runs automatically whenever we create a new instance based on the Dog class. 
# make sure to use TWO UNDERSCORES on either side of the method name
    def __init__(self, name, age):
        # define variables 
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


#create instance
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print("\n")

your_dog = Dog('Lucy', 3)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()

