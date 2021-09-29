PersonInfo = {
    'first name' : 'hanna',
    'last name' : 'cho',
    'age' : 30,
    'birthday' : 'september',
    'gender' : 'female'
}

print(PersonInfo['first name'].title())
print(PersonInfo['last name'].title())
print(PersonInfo['age'])
print(PersonInfo['birthday'].title())
print(PersonInfo['gender'])

number = {}
number['hanna'] = 2
number['nathan'] = 100
number['melanie'] = 22
number['eric'] = 5

print(number)

del number['hanna']

print(number)
print(number.keys())
print(f"\nNathan's favorite number is {number['nathan']}")

number_value = number.get('john', 'No favorite number stored')
print(number_value)


print("\n")
#looping through a dictionary
baseball = {
    'arod' : 0.41,
    'djeter' : 0.32,
    'ccsabathia' : 0.53,
    'cpark' : 0.53,
    'bruth' : 0.74
}

for player, percentage in baseball.items():
    print(player, percentage)


#looping through all the keys
print("\nList of Players:")
for player in baseball:
    print(f'{player.title()}')

for player in baseball.keys():
    if 'arod' in player:
        print (f"\n{player.title()} is a high value player")

print("\nList of Players-Alphabetical:")
for player in sorted(baseball.keys()):
    print(player.title())

#looping through values 
for score in baseball.values():
    print (score)

print("\n")
#get rid of duplicates on list
for score in set(baseball.values()):
    print(score)
