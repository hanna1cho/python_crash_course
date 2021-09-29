#Chapter 3 - Lists
friends = ['kelsey', 'aygul', 'mike', 'penelope', 'jack']
print(friends[0])
print(friends[-1])
print(friends[-2])
print(friends[3].title())

message = f'Hi {friends[0].title()}, thank you for coming to my birthday last week. I hope you had a great time.'
print(message)

guest_list = ['Harry', 'Neville', 'Ron', 'Hermione', 'Hagrid']
print(guest_list)

guest_list[4] = 'Sirius'
print(guest_list)

guest_list.insert(0, 'Luna')
guest_list.insert(3, 'Malfoy')
guest_list.append('Dumbledore')
print(guest_list)

deleted_person = guest_list.pop(0)
deleted_person1 = guest_list.pop(0)
deleted_person2 = guest_list.pop(0)
deleted_person3 = guest_list.pop(0)
print(f'Hi {deleted_person}, I am so sorry but we have limited seating and we can no longer have you at dinner.')
print(f'Hi {deleted_person1}, I am so sorry but we have limited seating and we can no longer have you at dinner.')
print(f'Hi {deleted_person2}, I am so sorry but we have limited seating and we can no longer have you at dinner.')
print(f'Hi {deleted_person3}, I am so sorry but we have limited seating and we can no longer have you at dinner.')

print(guest_list)

del guest_list[0]
del guest_list[0]


print(guest_list)

party_count = len(guest_list)
print(f'Current invitation list contains {party_count} people.')
