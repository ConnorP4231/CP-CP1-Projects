# Connor Pavicic, Calculator

calculation = input("What type of calculator do you want to perform? (+, -, *, /, **, %, //):")

if calculation == "+":
    first_add = int(input("What is the first number that you want to add?: "))
    second_add = int(input("What is the second number that you want to add?: "))
    print(first_add+second_add)
elif calculation == "-":
    first_sub = int(input("What is the first number you would like to subtract?: "))
    second_sub = int(input("What is the second number you would like to subtract?: "))
    print(first_sub-second_sub)
elif calculation == "*":
    first_mult = int(input("What is the first number you would like to multiply?: "))
    second_mult = int(input("What is the second number you would like to multiply?: "))
    print(first_mult*second_mult)
elif calculation == "/":
    first_div = int(input("What is the first number you would like to divide?: "))
    second_div = int(input("What is the second number you would like to divide?: "))
    print(first_div/second_div)
elif calculation == "**":
    first_ex = int(input("What do you want your base to be?: "))
    second_ex = int(input("What do you want your exponent to be?: "))
    print(first_ex**second_ex)
elif calculation == "%":
    first_mod = int(input("What is the first number you would like to divide?: "))
    second_mod = int(input("what is the second number you would like to divide?; "))
    print(first_mod%second_mod)
elif calculation == "//":
    first_floor = int(input("What is the first number you would like to divide?: "))
    second_floor = int(input("What is the second number you would like to divide?: "))
    print(first_floor//second_floor)