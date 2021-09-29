class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open.")

restaurant = Restaurant('Bengal Tiger', 'Indian')

class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['vanilla','strawberry','chocolate']

    def display_flavors(self):
        print(f"{self.name} serves {self.cuisine}.")
        print(f"{self.name}'s flavors are:")
        for flavor in self.flavors:
            print(flavor.title())

new_place = IceCreamStand('Hagendaz', 'ice cream')
new_place.display_flavors()