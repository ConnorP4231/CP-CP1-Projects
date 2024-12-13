# Connor Pavicic, finalGame
import random

while True:
    first_key = False
    first_door = False
    second_door = False
    hallway_door = False
    last_key = False
    last_door = False

    while True:
        def room_one():
            return """You found a riddle to find a key!
                    It says to get hurt and it will reward you..."""
        
        def room_two():
            return """This is the bathroom, it doesn't have anything special in it."""
        
        def room_three():
            return "This is a cramped room with nothing in it."
        
        def room_four():
            if first_key == True:
                return "Oh no! This is the trap room, you lost 10 health!"
            else:
                first_key = True
                return """Oh no! This is the trap room, you lost 10 health!
                        Wait, you found a key!"""
        
        def room_five():
            return "This is the safe room, nothing can hurt you here."
        
        def secret_room_one():
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
            
        def secret_room_two():
            if first_door == False:
                return "You need to unlock the first secret door first."
            if first_door == True and second_door == False:
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