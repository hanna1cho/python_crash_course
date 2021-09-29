class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open.")

restaurant = Restaurant('Bengal Tiger', 'Indian')

print(f"{restaurant.name} is in NYC.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n")
burger_place = Restaurant("Firebell", 'Burger')
burger_place.describe_restaurant()

print("\n")
seoul_restaurant = Restaurant('Crystal Jade', 'Chinese')
seoul_restaurant.describe_restaurant()

class User:
    def __init__(self, first_name, last_name, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is a {self.occupation}.")

    def greet_user(self):
        print(f"Hi {self.first_name}, welcome to the company.")

new_user = User('Harry', 'Potter', 'Wizard')
new_user.describe_user()

another_user = User('Paul', 'Hollywood', 'Celebrity Baker')
another_user.describe_user()
another_user.greet_user()