# Connor Pavicic, TicTacToe

import random

count = 1
num = input('enter num: ')

for rows in range(3):
    for columns in range(3):
        print(count, end=' ')
        count += 1
    print()

for rows in range(3):
    for columns in range(3):
        for num in rows or num in columns:
            print('X')
        else:
            print(count, end='')
            count += 1
    print()