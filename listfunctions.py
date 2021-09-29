# passing a list
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}."
        print(msg)

users = ['hanna', 'taylor', 'ginnie']
greet_users(users)

# modifying a list in a function
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        inprogress = unprinted_designs.pop()
        print(f'\nPrinting in progress: {inprogress}')
        completed_models.append(inprogress)


def show_completed(completed_models):
    print("\nFollowing models have been printed:")
    for completed in completed_models:
        print(completed)

unprinted_designs = ['stripes', 'sea creatures', 'purple sky']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed(completed_models)


# preventing a function for modifying list by passing a copy of the list as an argument to the function

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        inprogress = unprinted_designs.pop()
        print(f'\nPrinting in progress: {inprogress}')
        completed_models.append(inprogress)


def show_completed(completed_models):
    print("\nFollowing models have been printed:")
    for completed in completed_models:
        print(completed)

unprinted_designs = ['stripes', 'sea creatures', 'purple sky']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed(completed_models)

print(f"\nNo change to original list: {unprinted_designs}")
