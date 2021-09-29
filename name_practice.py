#Chapter 2 of Python Crash Course - Variables and Simple Data Types
name = "hermione granger"
message = f"Hello, {name.title()}!"
print(message)

print(name.upper())
print(name.lower())
print(name.title())


print('Barack Obama once said, "The cynics may be the loudest voices - but I promise you, they will accomplish the least."')

famous_person = "Barack Obama"
new_message = f'{famous_person} once said, "The cynics may be the loudest voices - but I promise you, they will accomplish the least."'
print(new_message)

boy_name = "\n\tBarack   "
print(boy_name.lstrip())
print(boy_name.rstrip())
print(boy_name.strip())