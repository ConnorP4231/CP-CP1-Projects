# Connor Pavicic, Palandrom

word = input("Type is word to see if it is a palandrom: ")
word_length = (len(word)-1)

if word[0:word_length]==word[-1:-word_length-1]:
    print("this is a palandrom")
else:
    print("this is not a palandrom")


