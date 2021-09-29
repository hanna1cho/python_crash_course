usernames = ['admin', 'applecakes', 'xyzuser', 'puppylover', 'youngboi59']
for username in usernames:
    if username == 'admin':
        print(f'Hello {username}, would you like to see a status report?')
    else: 
        print(f'Hello {username}, thank you for logging in again.')

print("\n")

#checking if list is empty
usernames = []
if usernames:
    for username in usernames:
         print(f'Hello {username}, thank you for logging in again.')
else:
    print("We need to find some users!")

print("\n")

current_users = ['admin', 'applecakes', 'xyzuser', 'puppylover', 'youngboi59']
new_users = ['cutiepie', 'xyzuser', 'supergirl001', 'brooklyn.NY', 'puppylover']

for new_user in new_users:
    if new_user in current_users:
        print ("This ID is already taken. Please provide different username.")
    else: 
        print (f"Congratulations! '{new_user}' is available for use.")


print("\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for numb in numbers:
    if numb == 1:
        print("1st")
    elif numb == 2:
        print("2nd")
    elif numb == 3:
        print("3rd")
    else: 
        print(f"{numb}th")
