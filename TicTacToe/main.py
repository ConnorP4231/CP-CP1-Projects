# Connor Pavicic, TicTacToe

import random

rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
    count = 0
    #1 = 0 0
    #2 = 0 1
    #3 = 0 2
    #4 = 1 0
    #5 = 1 1
    #6 = 1 2
    #7 = 2 0
    #8 = 2 1
    #9 = 2 2

    num = input('Enter a number: ')

    if num == '1':
        for row in range(3):
            for column in range(3):
                if num == '1':
                    if row == 0 and column == 0:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('1')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if num == '2':
        for row in range(3):
            for column in range(3):
                if num == '2':
                    if row == 0 and column == 1:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('2')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if num == '3':
        for row in range(3):
            for column in range(3):
                if num == '3':
                    if row == 0 and column == 2:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('3')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if num == '4':
        for row in range(3):
            for column in range(3):
                if num == '4':
                    if row == 1 and column == 0:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('4')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if num == '5':
        for row in range(3):
            for column in range(3):
                if num == '5':
                    if row == 1 and column == 1:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('5')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if num == '6':
        for row in range(3):
            for column in range(3):
                if num == '6':
                    if row == 1 and column == 2:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('6')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if num == '7':
        for row in range(3):
            for column in range(3):
                if num == '7':
                    if row == 2 and column == 0:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('7')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if num == '8':
        for row in range(3):
            for column in range(3):
                if num == '8':
                    if row == 2 and column == 1:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('8')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if num == '9':
        for row in range(3):
            for column in range(3):
                if num == '9':
                    if row == 2 and column == 2:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('9')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()
    print()

    computer_choice = random.choice(choice)
    print(computer_choice)

    if computer_choice == '1':
        for row in range(3):
            for column in range(3):
                if computer_choice == '1':
                    if row == 0 and column == 0:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('1')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if computer_choice == '2':
        for row in range(3):
            for column in range(3):
                if computer_choice == '2':
                    if row == 0 and column == 1:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('2')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if computer_choice == '3':
        for row in range(3):
            for column in range(3):
                if computer_choice == '3':
                    if row == 0 and column == 2:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('3')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if computer_choice == '4':
        for row in range(3):
            for column in range(3):
                if computer_choice == '4':
                    if row == 1 and column == 0:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('4')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if computer_choice == '5':
        for row in range(3):
            for column in range(3):
                if computer_choice == '5':
                    if row == 1 and column == 1:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('5')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if computer_choice == '6':
        for row in range(3):
            for column in range(3):
                if computer_choice == '6':
                    if row == 1 and column == 2:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('6')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if computer_choice == '7':
        for row in range(3):
            for column in range(3):
                if computer_choice == '7':
                    if row == 2 and column == 0:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('7')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if computer_choice == '8':
        for row in range(3):
            for column in range(3):
                if computer_choice == '8':
                    if row == 2 and column == 1:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('8')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()

    if computer_choice == '9':
        for row in range(3):
            for column in range(3):
                if computer_choice == '9':
                    if row == 2 and column == 2:
                        print('X', end=' ')
                        rows[count] = 'X'
                        choice.remove('9')
                        count += 1
                    else:
                        print(rows[count], end=' ')
                        count += 1
            print()
    print()