# Connor Pavicic, pigLatin

import random

word_ask = input("What word would you like to translate?: ")

def shuffle():
    word_list = list(word_ask)
    random.shuffle(word_list)
    final_word = ''.join(word_list)
    return final_word


print(shuffle())