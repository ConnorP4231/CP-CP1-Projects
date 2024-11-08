# Connor Pavicic, passwordChecker

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

while True:
    password = input("Enter a password with at least 8 characters, at least 1 special character, and at least 1 number: ")
    if len(password) < 8:
        print("Password invalid: must be at least 8 characters.")
        continue

    has_special = any(char in special_characters for char in password)
    has_number = any(char in numbers for char in password)

    if not has_special:
        print("Password invalid: must contain at least one special character.")
        continue

    if not has_number:
        print("Password invalid: must contain at least one number.")
        continue

    print("Password is valid.")
    break