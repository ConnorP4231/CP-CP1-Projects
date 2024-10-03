# Connor Pavicic, pigLatin

def translator():    
    word = input("What do you want to translate?: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.split()
    num_of_words = len(word)
    num = 0


    while num_of_words>num:
        if word[num][0] in vowels:
            word[num][0] = word[-1]
            word[num] = word[num] + 'yay'
            num = num+1
        else:
            word[num] = word[num] + 'ay'
            num = num + 1
    translated_sentence = ''.join(word)
    return translated_sentence

print(translator)