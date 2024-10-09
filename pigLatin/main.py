# Connor Pavicic, pigLatin

def translator():
    word = input("What word would you like to translate?: ")
    num = 0
    new_word = word
    vowels = 'aeiouAEIOU'
    consonants = ''
    
    while num < len(word) and word[num] not in vowels:
        consonants += word[num]
        num += 1

    if num < len(word):
        new_word = word[num:] + consonants + 'ay'
    else:
        new_word = word + 'ay'
    
    return new_word

print(translator())