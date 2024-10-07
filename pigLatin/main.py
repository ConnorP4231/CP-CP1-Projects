# Connor Pavicic, pigLatin

def translator():
    word = input("What word would you like to translate?: ")
    num = 0
    new_word = word
    vowels = 'aeiou'
    while word[num] not in vowels:
        consonant = word[num]
        new_word = new_word[(num+1):] + consonant
        num = num+1
        if word[num] not in vowels:
            vowel = word[num]
            new_word = vowel + new_word
    else:
        final_word = new_word + 'ay'
    
    final_word = new_word + 'ay'
    return final_word


print(translator())