class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.tables_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open.")

    def read_tables_served(self):
        print(f"Tables served: {self.tables_served}")

    def update_servings(self, new_service):
        self.tables_served = new_service

    def increment_servings(self, addtl_tables):
        self.tables_served += addtl_tables

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
seoul_restaurant.read_tables_served()
seoul_restaurant.tables_served = 11
seoul_restaurant.read_tables_served()
seoul_restaurant.update_servings(9)
seoul_restaurant.read_tables_served()
seoul_restaurant.increment_servings(10)
seoul_restaurant.read_tables_served()


