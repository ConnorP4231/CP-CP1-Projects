# Connor Pavicic, pigLatin

def translator(word_slice):    
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
            word_slice = word[num][0]
            if word_slice in word[num]:
                word[num] = word_slice
            word[num] += word_slice
    translated_sentence = ' '.join(word)
    return translated_sentence

print(translator(word_slice="word_slice"))