# Connor Pavicic, passwordChecker

num = 0
special_characters = '!@#$%&*'
numbers = '1234567890'

while num < 2:
    password = input("Enter a password with atleast 8 characters, atleast 1 special character, and atleast 1 number: ")
    num = 0
    length = len(password)

    if special_characters in password:
        num += 1
    if numbers in password:
        num += 1
    if length