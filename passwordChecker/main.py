# Connor Pavicic, passwordChecker

num = 0
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

while num < 3:
    password = list(input("Enter a password with atleast 8 characters, atleast 1 special character, and atleast 1 number: "))
    num = 0
    length = len(password)

    if special_characters in password:
        num += 1
    if numbers in password:
        num+=1
    if length <= 8:
        num += 1
    if num < 3:
        print("Password invalid, try again.")
else:
    print("Password is valid.")