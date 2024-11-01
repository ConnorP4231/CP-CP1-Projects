# Connor Pavicic, multTable

num = int(input("What number do you want to find multiples of?: "))

for multiple in range(1, num+1):
    if num/multiple != float(num):
        print(multiple)
    else:
        print('')