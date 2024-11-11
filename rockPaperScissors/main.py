# Connor Pavicic, rockPaperScissors

import random
rps_list = ['rock', 'paper', 'scissors']
human_score = 0
robot_score = 0

while True:
    rps = input("Rock, paper, or scissors?: ").lower()
    computer_rps = random.choice(rps_list)

    if rps == computer_rps:
            print('Computer chose', computer_rps, 'and you chose', rps, 'so it is a tie.')
    elif rps == 'rock' and computer_rps == 'paper':
            print('Computer chose', computer_rps, 'and you chose', rps, 'so the computer won.')
            robot_score += 1
            print('Your score is', human_score, 'and the robots score is', robot_score)
    elif rps == 'scissors' and computer_rps == 'paper':
            print('Computer chose', computer_rps, 'and you chose', rps, 'so you won.')
            human_score += 1
            print('Your score is', human_score, 'and the robots score is', robot_score)
    elif rps == 'scissors' and computer_rps == 'rock':
            print('Computer chose', computer_rps, 'and you chose', rps, 'so the computer won.')
            robot_score += 1
            print('Your score is', human_score, 'and the robots score is', robot_score)
    elif rps == 'paper' and computer_rps == 'rock':
            print('Computer chose', computer_rps, 'and you chose', rps, 'so you won.')
            human_score += 1
            print('Your score is', human_score, 'and the robots score is', robot_score)
    elif rps == 'paper' and computer_rps == 'scissors':
            print('Computer chose', computer_rps, 'and you chose', rps, 'so the computer won.')
            robot_score += 1
            print('Your score is', human_score, 'and the robots score is', robot_score)
    elif rps == 'rock' and computer_rps == 'scissors':
            print('Computer chose', computer_rps, 'and you chose', rps, 'so you won.')
            robot_score += 1
            print('Your score is', human_score, 'and the robots score is', robot_score)
    else:
        print("Invalid option.")

    play_again = input("Do you want to play again?: ")
    
    if play_again == 'yes':
        continue
    if play_again == 'no':
        print("The final score for you is", human_score, "and the robot ended with a score of", robot_score)
        break
    else:
        print("Invalid option, play again.")