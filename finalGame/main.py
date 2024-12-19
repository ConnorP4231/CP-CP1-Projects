# Connor Pavicic, finalGame

import random
import time

# Initializing the global game variables
first_key = False
first_door = False
second_door = False
hallway_door = False
last_key = False
final_door = False
sword = False

health = 100
thirst = 100
hunger = 100
play_again = ''

print("""Hello user, you have awoken in a random house that has creatures lurking around in it. 
Your task is to escape this house by reading notes to unlock doors and all that. Good luck!""")

def reset_game():
    global first_key, first_door, second_door, hallway_door, last_key, final_door, sword, health, thirst, hunger, play_again
    first_key = False
    first_door = False
    second_door = False
    hallway_door = False
    last_key = False
    final_door = False
    sword = False

    health = 100
    thirst = 100
    hunger = 100
    play_again = ''

def check_game_over():
    global health, hunger, thirst, play_again
    if health <= 0:
        print('Your health hit zero and you died.')
        while True:
            play_again_input = input('Do you want to play again? (yes or no): ').lower()
            if play_again_input == 'yes':
                reset_game()
                break
            elif play_again_input == 'no':
                print('Ok thanks for playing!')
                play_again = play_again_input
                break
    elif hunger <= 0:
        print('Your hunger hit zero and you starved to death.')
        while True:
            play_again_input = input('Do you want to play again? (yes or no): ').lower()
            if play_again_input == 'yes':
                reset_game()
                break
            elif play_again_input == 'no':
                print('Ok thanks for playing!')
                play_again = play_again_input
                break
    elif thirst <= 0:
        print('You got too thirsty and died because of it.')
        while True:
            play_again_input = input('Do you want to play again? (yes or no): ').lower()
            if play_again_input == 'yes':
                reset_game()
                break
            elif play_again_input == 'no':
                print('Ok thanks for playing!')
                play_again = play_again_input
                break

def room_one():
    return """You found a riddle to find a key!
                It says to get hurt and it will reward you..."""

def room_two():
    return """This is the bathroom, it doesn't have anything special in it."""

def room_three():
    return "This is a cramped room with nothing in it."

def room_four():
    global first_key, health
    if first_key:
        health -= 10
        return f"Oh no! This is the trap room, you lost 10 health! Your health is now {health}"
    else:
        first_key = True
        health -= 10
        return f"""Oh no! This is the trap room, you lost 10 health!
                    Wait, you found a key! Your health is now: {health}"""

def room_five():
    return "This is the safe room, nothing can hurt you here."

def secret_room_one():
    global first_door, first_key, second_door
    if not first_door:
        if first_key:
            while True:
                room_two_pass = int(input("""You have unlocked the first secret room! Here is a note to help you find the password to the next door:
                            What is 963 divided by the sin of 3 rounded to the nearest whole number?: """))
                if room_two_pass == 6824:
                    break
                else:
                    continue
            if room_two_pass == 6824:
                second_door = True
                return 'Code correct! The next secret room is now unlocked!'
            else:
                return "Code incorrect."
        else:
            return "You need to find a key before you unlock this room."
    elif first_door and first_key:
        if not second_door:
                while True:
                    room_two_pass = int(input("""You are now in the first secret room! Here is a note to help you find the password to the next door:
                            What is 963 divided by the sin of 3 rounded to the nearest whole number?: """))
                    if room_two_pass == 6824:
                        break
                    else:
                        continue
                if room_two_pass == 6824:
                    second_door = True
                    return 'Code correct! The next secret room is now unlocked!'

def secret_room_two():
    global hallway_door
    if second_door == False:
        return "You haven't unlock this room yet."
    if second_door == True:
        print('You are now in the hallway.')
        if final_door == False:
            while True:
                halllway_pass = input('What is LeBron James middle name?:').lower()
                if halllway_pass == 'raymone':
                    break
                else:
                    continue
            if halllway_pass == 'raymone':
                hallway_door = True
                return 'Code correct! The hallway is now unlocked!'


def hallway():
    global hallway_door
    if hallway_door == False:
        return "You haven't unlocked this room yet."
    elif hallway_door == True:
        return """You are now in the hallway. Here is a note to help you find the last key: 
Go into the MOST dangerous place in this house..."""

def final_room():
    global hallway_door, last_key
    if final_door == False:
        return "You haven't unlocked this room yet."
    elif final_door == True:
        return "You unlocked the last door and escaped! Congratulations you won the game!"

# Main game loop
while True:
    check_game_over()
    which_room = int(input('Which room would you like to go to? (1-9): '))

    if which_room == 1:
        print(room_one())
    elif which_room == 2:
        print(room_two())
    elif which_room == 3:
        print(room_three())
    elif which_room == 4:
        print(room_four())
    elif which_room == 5:
        print(room_five())
    elif which_room == 7:
        print(secret_room_one())
    elif which_room == 8:
        print(secret_room_two())
    elif which_room == 9:
        print(hallway())
    elif which_room == 10:
        print(final_room())
        if hallway_door and last_key:
            while True:
                play_again_input = input('Do you want to play again? (yes or no): ').lower()
                if play_again_input == 'yes':
                    reset_game()
                    break
                elif play_again_input == 'no':
                    print('Ok thanks for playing!')
                    play_again = play_again_input
                    break 
    elif which_room == 6:
        if hallway_door:
            print("You found a key! But wait... This is the creature hideout! Defend yourself!")
            last_key = True
        else:
            print('This is the creature hideout! Defend yourself!')

        if sword == False:
            sword_option = input('Do you want to lose 10 health for a sword to increase your odds of winning? (yes or no): ').lower()
            if sword_option == 'yes':
                sword = True
                health -= 10
                print('Ok, fight starts... now!')
                for i in range(3):
                    print('*epic battle moves*')
                    time.sleep(1)
                num = random.randint(1, 2)
                if num == 1:
                    health -= 20
                    print(f'You won the battle! However the creature took a lot of health from you, your health is {health}')
                    final_door = True
                else:
                    print('You lost the battle and died.')
                    while True:
                        play_again_input = input('Do you want to play again? (yes or no): ').lower()
                        if play_again_input == 'yes':
                            reset_game()
                            break
                        elif play_again_input == 'no':
                            print('Ok thanks for playing!')
                            play_again = play_again_input
                            break
            else:
                print('Ok, fight starts... now!')
                for i in range(3):
                    print('*epic battle moves*')
                    time.sleep(1)
                num = random.randint(1, 4)
                if num == 3:
                    health -= 20
                    print(f'You won the battle! However the creature took a lot of health from you, your health is {health}')
                else:
                    print('You lost the battle and died.')
                    while True:
                        play_again_input = input('Do you want to play again? (yes or no): ').lower()
                        if play_again_input == 'yes':
                            reset_game()
                            break
                        elif play_again_input == 'no':
                            print('Ok thanks for playing!')
                            play_again = play_again_input
                            break

        elif sword:
            print('Ok, fight starts... now!')
            for i in range(3):
                print('*epic battle moves*')
                time.sleep(1)
            num = random.randint(1, 2)
            if num == 1:
                health -= 20
                print(f'You won the battle! However the creature took a lot of health from you, your health is {health}')
                final_door = True
            else:
                print('You lost the battle and died.')
                while True:
                        play_again_input = input('Do you want to play again? (yes or no): ').lower()
                        if play_again_input == 'yes':
                            reset_game()
                            break
                        elif play_again_input == 'no':
                            print('Ok thanks for playing!')
                            play_again = play_again_input
                            break

    if play_again == 'no':
        break
    else:
        thirst -= 2
        hunger -= 2
        print(f'Your thirst is now {thirst}')
        print(f'Your hunger is now {hunger}')
        
        health_increase_chance = random.randint(1, 10)
        if health_increase_chance == 4:
            health += 5
            if health > 100:
                health = 100
            print(f'You found a health boost that increased your health by 5! Your health is now {health}')

        health_decrease_chance = random.randint(1, 5)
        if health_decrease_chance == 2:
            health -= 5
            print(f'You encountered a tiny monster and easily killed it off, however it took 5 health from you, your health is now: {health}')
        
        hunger_increase_chance = random.randint(1, 15)
        if hunger_increase_chance == 9:
            hunger += 7
            if hunger > 100:
                hunger = 100
            print(f'You found some old food and it increased your hunger, it is now {hunger}')
        
        thirst_increase_chance = random.randint(1, 15)
        if thirst_increase_chance == 9:
            thirst += 7
            if thirst > 100:
                thirst = 100
            print(f'You found some still water and drank it. Your thirst is now {thirst}')
