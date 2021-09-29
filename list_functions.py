#list comprehension
squares = [value**2 for value in range(1, 9)]
print(squares)

#counting to twenty
for value in range(1, 21):
	print(value)

numbers = list(range(1, 1001))
print(numbers)

million = list(range(0, 1000001))
print(min(million))
print(max(million))
print(sum(million))


for odd in range(1, 20, 2):
	print(odd)

for mult in range (3, 31, 3):
	print(mult)


cube = list(range(1, 11))
for num in cube:
	num1 = num**3
	print(num1)

cubes = [value**3 for value in range(1, 11)]
print(cubes)

#slicing a list
players = ['ellie', 'michael', 'tim', 'cathy', 'jessica']
print(players[0:2]) #print player[0] and player[1]
print(players[:4])
print(players[2:])
print(players[-3:])

print("\nHere are the first three players on my team:")
for player in players[0:3]:
	print(player.title())

#copying a list [:]

school_supply = ['Pencil', 'Calculator', 'Ruler', 'Notebook', 'Glue']
required = school_supply[:]

print("\nSpring semeter school supply list includes")
print(school_supply)
print("\nRequired items are")
print(required)

school_supply.append("Laptop")
required.append("Crayons")

print(school_supply)
print(required)
