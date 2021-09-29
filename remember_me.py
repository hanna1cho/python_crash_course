import json

def get_stored_username():
    """get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None 
    else: 
        return username


def get_new_username():
    """prompt for a new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
            json.dump(username, f)
    return username
            

def greet_user():
    """greet the user by name"""
    username = get_stored_username()
    if username:
        confirm = input(f"Hi, are you {username}?" )
        if confirm == 'yes':
            print(f"Hi {username}, welcome back!")
        else: 
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
       username = get_new_username()
       print(f"We'll remember you when you come back, {username}!")

greet_user()