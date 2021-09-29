travel_wish = ['Utah', 'Egypt', 'Milan', 'Paris', 'Bangkok', 'Kyoto', 'Hawaii']
print(travel_wish)

#sort in alphabetical order without affecting original list
print(sorted(travel_wish))
print(f'{travel_wish}\n')


#sort in reverse alphabetical order without affecting original list
print(sorted(travel_wish, reverse=True))
print(f'{travel_wish}\n')

#reverse the order of the list
travel_wish.reverse()
print(f'{travel_wish}\n')

#reverse back the order of the list
travel_wish.reverse()
print(f'{travel_wish}\n')

travel_wish.sort()
print(f'{travel_wish}\n')

travel_wish.sort(reverse=True)
print(f'{travel_wish}\n')


rand_num = [1, 209, 398, 3, 8, 22, 76, 14]

rand_num.append(35)
print(rand_num)
print(sorted(rand_num))

rand_num[2] = 311
print(rand_num)

del rand_num[0]
print(rand_num)

rand_num.insert(0, 1)
print(rand_num)

rand_num.remove(76)
print(rand_num)

print(len(rand_num))

fav_num = rand_num.pop(0)
print(rand_num)
print(f'{fav_num}\n')

rand_num.reverse()
print(f'{rand_num}\n')

rand_num.sort()
print(f'{rand_num}\n')

rand_num.sort(reverse=True)
print(f'{rand_num}\n')