# Connor Pavicic, TicTacToe

import random

#1 = 0 0
#2 = 0 1
#3 = 0 2
#4 = 1 0
#5 = 1 1
#6 = 1 2
#7 = 2 0
#8 = 2 1
#9 = 2 2

for row in range(3):
    for column in range(3):
        if row == 1 and column == 0:
            print('-', end=' ')
        else:
            print('*', end=' ')
    print()