# Connor Pavicic, characterCreator

race = input("Which race do you want to be? (Example: Humans, Elves, Dwarves, or Halflings.): ")
race_class = input("Which class do you want your rac to be? (Example: Rouge, Paleden, Ranger, Warrior, Wizard): ")
health = 0
strength = 0
dexterity = 0
intelligence = 0

if race_class.lower() == 'rouge':
    dexterity += 7
elif race_class.lower() == 'paleden':
    strength += 5
    health += 3
    intelligence -= 2
elif race_class.lower() == 'ranger':
    dexterity += 10
elif race_class.lower() == 'warrior':
    health += 7
    strength += 5
elif race_class.lower() == 'wizard':
    intelligence += 10
else:
    print("That is not a class.")

def Humans(health, strength, dexterity, intelligence):
    health += 85
    strength += 68
    dexterity += 84
    intelligence += 79

    if health > 100:
        health = 100
    elif strength > 100:
        strength = 100
    elif dexterity > 100:
        dexterity = 100
    elif intelligence > 100:
        intelligence = 100
    
    return """
Your Stats:

Health: {}/100
Strength: {}/100
Dexterity: {}/100
Intelligence: {}/100""".format(health, strength, dexterity, intelligence)



def Elves(health, strength, dexterity, intelligence):
    health += 63
    strength += 58
    dexterity += 99
    intelligence += 95

    if health > 100:
        health = 100
    elif strength > 100:
        strength = 100
    elif dexterity > 100:
        dexterity = 100
    elif intelligence > 100:
        intelligence = 100
    
    return """
Your Stats:

Health: {}/100
Strength: {}/100
Dexterity: {}/100
Intelligence: {}/100""".format(health, strength, dexterity, intelligence)

def Dwarves(health, strength, dexterity, intelligence):
    health += 70
    strength += 58
    dexterity += 78
    intelligence += 80

    if health > 100:
        health = 100
    elif strength > 100:
        strength = 100
    elif dexterity > 100:
        dexterity = 100
    elif intelligence > 100:
        intelligence = 100
    
    return """
Your Stats:

Health: {}/100
Strength: {}/100
Dexterity: {}/100
Intelligence: {}/100""".format(health, strength, dexterity, intelligence)

def Halflings(health, strength, dexterity, intelligence):
    health += 89
    strength += 81
    dexterity += 91
    intelligence += 43

    if health > 100:
        health = 100
    elif strength > 100:
        strength = 100
    elif dexterity > 100:
        dexterity = 100
    elif intelligence > 100:
        intelligence = 100
    
    return """
Your Stats:

Health: {}/100
Strength: {}/100
Dexterity: {}/100
Intelligence: {}/100""".format(health, strength, dexterity, intelligence)

if race.lower() == 'humans':
    print(Humans(health, strength, dexterity, intelligence))
elif race.lower() == 'elves':
    print(Elves(health, strength, dexterity, intelligence))
elif race.lower() == 'dwarves':
    print(Dwarves(health, strength, dexterity, intelligence))
elif race.lower() == 'halflings':
    print(Halflings(health, strength, dexterity, intelligence))
else:
    print('That is not a character.')

race_class = input("What class do you want to be? (Example: Rouge, Paleden, Ranger, Warrior, Wizard): ")