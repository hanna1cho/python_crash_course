import json

# def save_favorite_number():
#     favorite_number = input("What is your favorite number? ")
#     filename = 'number.json'
#     with open(filename, 'w') as f:
#         json.dump(favorite_number, f)

# def read_favorite_number():
#     filename = 'number.json'
#     with open(filename, 'r') as f:
#         favorite_number = json.load(f)
#         print(f"I know your favorite number! It's {favorite_number}.")

# save_favorite_number()
# read_favorite_number()

def favorite_number():
    filename = 'number.json'
    try: 
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        favorite_number = input("What is your favorite number? ")
        with open(filename, 'w') as f:
            json.dump(favorite_number, f)
    else:
        print(f"I know your favorite number! It's {number}.")

favorite_number()