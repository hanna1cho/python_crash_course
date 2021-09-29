class User:
    def __init__(self, first_name, last_name, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is a {self.occupation}.")

    def greet_user(self):
        print(f"Hi {self.first_name}, thank you for visiting the website.")

    def increment_login(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        if self.login_attempts != 0:
            self.login_attempts = 0




new_user = User('Harry', 'Potter', 'Wizard')
new_user.describe_user()

another_user = User('Paul', 'Hollywood', 'Celebrity Baker')
another_user.describe_user()
another_user.greet_user()

another_user.increment_login()
another_user.increment_login()
another_user.increment_login()
print(another_user.login_attempts)

another_user.reset_login_attempts()
print(another_user.login_attempts)
