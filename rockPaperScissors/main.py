# Connor Pavicic, rockPaperScissors

import random
rps_list = ['rock', 'paper', 'scissors']

while True:
    rps = input("Rock, paper, or scissors?: ").lower()
    computer_rps = random.choice(rps_list)
    if rps != 'rock' and rps != 'paper' and rps != 'scissors':
        print("Invalid option, ")
        play_again = input("Do you want to play again?: ").lower()
        if play_again == 'yes':
            continue
        elif play_again == 'no':
            break
        else:
            play_again = input("Do you want to play again?: ").lower()
    else:
        if rps == computer_rps:
            print('Computer chose', computer_rps, 'and you chose', rps, 'so it is a tie.')
        elif rps == 'rock' and computer_rps == 'paper':
            print('Computer chose', computer_rps, 'and you chose', rps, 'so the computer won.')
        elif rps == 'scissors' and computer_rps == 'paper':
            print('Computer chose', computer_rps, 'and you chose', rps, 'so you won.')
        elif rps == 'scissors' and computer_rps == 'rock':
            print('Computer chose', computer_rps, 'and you chose', rps, 'so the computer won.')
        elif rps == 'paper' and computer_rps == 'rock':
            print('Computer chose', computer_rps, 'and you chose', rps, 'so you won.')
        elif rps == 'paper' and computer_rps == 'scissors':
            print('Computer chose', computer_rps, 'and you chose', rps, 'so the computer won.')
        elif rps == 'rock' and computer_rps == 'scissors':
            print('Computer chose', computer_rps, 'and you chose', rps, 'so you won.')
        
        play_again = input("Do you want to play again?: ").lower()
        
        while play_again != 'yes' or play_again != 'no':
            if play_again == 'yes':
                continue
            elif play_again == 'no':
                break