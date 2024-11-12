# Connor Pavicic, errorCalculator

calculation = input("What type of calculation do you want to perform? (+, -, *, /, **, %, //):")

if calculation == "+":
    first_add = input("What is the first number that you want to add?: ")
    second_add = input("What is the second number that you want to add?: ")
    try:
        int(first_add) + int(second_add)
    except:
        print("You have to enter whole numbers.")
    else:
        print(int(first_add) + int(second_add))
elif calculation == "-":
    first_sub = input("What is the first number you would like to subtract?: ")
    second_sub = input("What is the second number you would like to subtract?: ")
    try:
        int(first_sub) - int(second_sub)
    except:
        print("You have to enter whole numbers.")
    else:
        print(int(first_sub)-int(second_sub))
elif calculation == "*":
    first_mult = input("What is the first number you would like to multiply?: ")
    second_mult = input("What is the second number you would like to multiply?: ")
    try:
        int(first_mult) * int(second_mult)
    except:
        print('You have to enter whole numbers.')
    else:
        print(int(first_mult)*int(second_mult))
elif calculation == "/":
    first_div = input("What is the first number you would like to divide?: ")
    second_div = input("What is the second number you would like to divide?: ")
    if second_div == '0':
        print('You can not divide by 0')
    else:
        try:
            int(first_div)/int(second_div)
        except:
            print('You have to enter whole numbers.')
        else:
            print(int(first_div)/int(second_div))
elif calculation == "**":
    first_ex = input("What do you want your base to be?: ")
    second_ex = input("What do you want your exponent to be?: ")
    try:
        int(first_ex)**int(second_ex)
    except:
        print('You can only enter whole numbers.')
    else:
        print(int(first_ex)**int(second_ex))
elif calculation == "%":
    first_mod = input("What is the first number you would like to divide?: ")
    second_mod = input("what is the second number you would like to divide?; ")
    try:
        int(first_mod)%int(second_mod)
    except:
        print('You can only enter whole numbers.')
    else:
        print(int(first_mod)%int(second_mod))
elif calculation == "//":
    first_floor = input("What is the first number you would like to divide?: ")
    second_floor = input("What is the second number you would like to divide?: ")
    if second_floor == '0':
        print('You can not divide by 0')
    else:
        try:
            int(first_floor)//int(second_floor)
        except:
            print('You can only enter whole numbers.')
        else:
            print(int(first_floor)//int(second_floor))
else:
    print('That is not an option, try again.')
