# Connor Pavicic, TicTacToe

import random

while True:
    move_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    count = 1

    move = int(input('Where do you want to go? (1,2,3,4,5,6,7,8,9): '))
    move_list.remove(move)

    for rows in range(3):
        for columns in range(3):
            print(count, end=' ')
        print()
    print()
    
    if move == 1:
        for rows in range(3):
            for columns in range(3):
                if move == 1:
                    continue
                print('O')
            else:
                print(count, end=' ')