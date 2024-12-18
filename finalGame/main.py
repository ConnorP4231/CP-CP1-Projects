# Connor Pavicic, finalGame
import random
import time

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

while True:
    if play_again == 'yes':
        pass
    elif play_again == 'no':
        break

    if health == 0:
        print('Your health hit zero and you died. ')
        while True:
                play_again_input = input('Do you want to play again? (yes or no): ').lower()
                if play_again_input == 'yes':
                    play_again = play_again_input
                    break
                elif play_again_input == 'no':
                    print('Ok thanks for playing!')
                    play_again = play_again_input
                    break
                else:
                    print('Incorrect option, try again.')
    if hunger == 0:
        print('Your hunger hit zero and you starved to death.')
        while True:
                play_again_input = input('Do you want to play again? (yes or no): ').lower()
                if play_again_input == 'yes':
                    play_again = play_again_input
                    break
                elif play_again_input == 'no':
                    print('Ok thanks for playing!')
                    play_again = play_again_input
                    break
                else:
                    print('Incorrect option, try again.')
    
    if thirst == 0:
        print('You got too thirsty and died because of it.')
        while True:
                play_again_input = input('Do you want to play again? (yes or no): ').lower()
                if play_again_input == 'yes':
                    play_again = play_again_input
                    break
                elif play_again_input == 'no':
                    print('Ok thanks for playing!')
                    play_again = play_again_input
                    break
                else:
                    print('Incorrect option, try again.')
    
    
    def room_one():
        return """You found a riddle to find a key!
                It says to get hurt and it will reward you..."""
    
    def room_two():
        return """This is the bathroom, it doesn't have anything special in it."""
    
    def room_three():
        return "This is a cramped room with nothing in it."
    
    def room_four(first_key = first_key, health = health):
        if first_key == True:
            health -= 10
            return f"Oh no! This is the trap room, you lost 10 health! Your health is now {health}"
        else:
            first_key = True
            health -= 10
            return f"""Oh no! This is the trap room, you lost 10 health!
                    Wait, you found a key! Your health is now: {health}"""
    
    def room_five():
        return "This is the safe room, nothing can hurt you here."
    
    def secret_room_one(first_door = first_door, first_key = first_key, second_door = second_door):
        if first_door == False:
            if first_key == True:
                return """You have unlocked the first secret room! Here is a note to help you find the password to the next door:
                        What is 963 divided by the sin of 3 rounded to the nearest whole number?"""
            elif first_key == False:
                return "You need to find a key before you unlock this room."
        elif first_door == True and first_key == True:
            if second_door == False:
                return """You are now in the first secret room. Here is a note to help you find the password to the next door:
                        What is 963 divided by the sin of 3 rounded to the nearest whole number?"""
        
    def secret_room_two(first_door = first_door, second_door = second_door, hallway_door = hallway_door):
        if first_door == False:
            return "You need to unlock the first secret door first."
        if first_door == True and second_door == False:
            while second_door == False:
                room_two_pass = int(input('What is the password?: '))
                if room_two_pass == 6824:
                    second_door = True
                    return """Password correct! You have now unlocked the second secret door. Here is a note to unlock the hallway door:
                            Who was the 2nd president of Uzbekistan?"""
                elif room_two_pass != 6824:
                    return "Code incorrect."
        elif second_door == True:
            if hallway_door == False:
                return """You are now in the second secret room. Here is a note to unlock the hallway door:
                            Who was the 2nd president of Uzbekistan?"""
            else:
                return "You are now in the second secret room."
                
    def hallway(second_door = second_door, hallway_door = hallway_door):
        if second_door == False:
            return "You haven't unlocked this room yet."
        if second_door == True and hallway_door == False:
            while hallway_door == False:
                hallway_code = input('Who was the second leader of Uzbekistan?: ').lower()
                if hallway_code == 'kuprian kirkizh':
                    hallway_door = True
                    return """Password correct! You are now in the hallway. Here is a note to find the last key: 
                            You will need to fight a creature to obtain this key..."""
                elif hallway_code != 'kuprian kirkizh':
                    return "Code incorrect."
        else:
            return "You are now in the hallway."
            
    def final_room(hallway_door = hallway_door, last_key = last_key):
        if hallway_door == False:
            return "You haven't unlocked this room yet."
        if hallway_door == True and last_key == False:
            return """You have to find a key first. Here is a note to find that key:
                        You will need to fight a creature to obtain this key."""
        if hallway_door == True and last_key == True:
            return "You won the game and a $2.47 Subway gift card!"
        
    which_room = int(input('Which room would you like to go to?: '))

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
        print(final_room())
        if hallway_door == True and last_key == True:
            while True:
                    play_again_input = input('Do you want to play again? (yes or no): ').lower()
                    if play_again_input == 'yes':
                        play_again = play_again_input
                        break
                    elif play_again_input == 'no':
                        print('Ok thanks for playing!')
                        play_again = play_again_input
                        break
                    else:
                        print('Incorrect option, try again.')
    elif which_room == 6:
        if hallway_door == True:
            print("You found a key! But wait... This is the creature hideout! Defend yourself!")
            first_key = True
        elif hallway_door == False:
            print('This is the create hideout! Defend yourself!')
        
        if sword == False:
            sword_option = input('Do you want to lose 10 health for a sword to increase your odds of winning? (yes or no): ').lower()
            if sword_option == 'yes':
                sword == True
                health -= 10
                print('Ok, fight starts... now!')
                for i in range(3):
                    print('*epic battle moves*')
                    time.sleep(1)
                num = random.randint(1, 2)
                if num == 1:
                    print('You won the battle!')
                else:
                    print('You lost the battle and died.')
                    while True:
                        play_again_input = input('Do you want to play again? (yes or no): ').lower()
                        if play_again_input == 'yes':
                            play_again = play_again_input
                            break
                        elif play_again_input == 'no':
                            print('Ok thanks for playing!')
                            play_again = play_again_input
                            break
                        else:
                            print('Incorrect option, try again.')
                    
            else:
                print('Ok, fight starts... now!')
                for i in range(3):
                    print('*epic battle moves*')
                    time.sleep(1)
                num = random.randint(1, 4)
                if num == 3:
                    print('You won the battle!')
                else:
                    print('You lost the battle and died.')
                    while True:
                        play_again_input = input('Do you want to play again? (yes or no): ').lower()
                        if play_again_input == 'yes':
                            play_again = play_again_input
                            break
                        elif play_again_input == 'no':
                            print('Ok thanks for playing!')
                            play_again = play_again_input
                            break
                        else:
                            print('Incorrect option, try again.')
        elif sword == True:
            print('Ok, fight starts... now!')
            for i in range(3):
                print('*epic battle moves*')
                time.sleep(1)
            num = random.randint(1, 2)
            if num == 1:
                print('You won the battle!')
            else:
                print('You lost the battle and died.')
                while True:
                        play_again_input = input('Do you want to play again? (yes or no): ').lower()
                        if play_again_input == 'yes':
                            play_again = play_again_input
                            break
                        elif play_again_input == 'no':
                            print('Ok thanks for playing!')
                            play_again = play_again_input
                            break
                        else:
                            print('Incorrect option, try again.')

    
    thirst -= 2
    print(f'Your thirst went down and it is now {thirst}')
    hunger -= 2
    print(f'Your hunger went down and it is now {thirst}')
    
    
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