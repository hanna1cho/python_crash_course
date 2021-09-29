name = "luna lovegood"
print(name.title())
print(name.upper())
print(name.lower())


first_name = "luna"
last_name = "lovegood"
full_name = f"{first_name} {last_name}"
print(full_name.title())
print(f"Hello, {full_name.title()}")


message = f"Hello, {full_name.title()}!"
print(message)

print("Fruits:\nApple\nOrange\nBanana\nWatermelon")

print("\nFruits:\n\tPear\n\tTangerine\n\tCherry\n\tLemon")

favorite_language = "Python  "
favorite_language.rstrip()
print(favorite_language.rstrip())

not_favorite_language = "  C#"
not_favorite_language.lstrip()
print(not_favorite_language.lstrip())

easy_language = "  English   "
easy_language.strip()
print(easy_language.strip())