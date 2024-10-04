# Connor Pavicic, pigLatin

def translator():    
    word = input("What do you want to translate?: ")
    word = word[1:] + word[0] + 'ay'
    print(word)


translator()