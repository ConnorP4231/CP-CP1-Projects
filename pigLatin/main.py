# Connor Pavicic, pigLatin

def translator():    
    word = input("What do you want to translate?: ")
    vowels = 'aeiou'
    num = 0
    length_word = len(word)-1
   
    if vowels in word[0]:
        word = word + 'ay'
        print(word)
    else:
       while length_word>num:
            while vowels not in word[num]:
                word = word[num+1:] + word[num]
                num = num+1
            else:
                word = word + 'ay'
                print(word)


translator()