# Connor Pavicic, multTable

num = int(input("What number do you want to find multiples of?: "))

for mult in range(1, 13):
    if num % mult == 0:
        print(mult)