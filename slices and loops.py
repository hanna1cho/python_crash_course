CandleScents = ['jasmine', 'vanilla', 'birthday cake', 'rose garden', 'green tea', 'rain forest', 'lemons and peaches']
print(CandleScents[:3])
print(CandleScents[2:5])
print(CandleScents[-3:])

pizza = ['margherita', 'pepperoni', 'baked ziti', 'broccoli', 'proscuitto']
friend_pizza = pizza[:]
print('\n')
print(pizza)
print(friend_pizza)

pizza.append('chocolate')
friend_pizza.append('buffalo chicken')
print('\n')
print(pizza)
print(friend_pizza)
print('\n')

foods = ['spaghetti', 'sushi', 'noodle soup', 'hamburger']
for food in foods:
	print(food)

for food in foods:
	print(f'Is {food} your favorite food?')