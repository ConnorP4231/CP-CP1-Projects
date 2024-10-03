# Connor Pavicic, pigLatin

def translator():    
    word = input("What do you want to translate?: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.split()
    num_of_words = len(word)
    num = 0
    
    while num_of_words>num:
        if word[num][0].lower() in vowels:
            word[num] = word[num] + 'yay'
            num = num+1
        else:
            global word_split
            global first_char
            first_char = word[num][0]
            word[num] = str(word[num])
            word_split = word[num][0].split
            word_split = str(word_split)
            word[num] = word[num][0].replace(first_char, '')
            word[num] = word[num] + word_split + 'ay'
            word[num] = list(word[num])
    
    global translated
    translated = word
    return translated


print(translator)