# Connor Pavicic, Palandrom

word = input("Type is word to see if it is a palandrom: ")
word_length = len(word)
negative_length = -1*word_length

if word[0:word_length]==word[0:negative_length]:
    print("this is a palandrom")
else:
    print("this is not a palandrom")

