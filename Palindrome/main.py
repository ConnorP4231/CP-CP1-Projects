# Connor Pavicic, Palindrome

word = input("What word do you want to check to see if it is a palindrome?: ")
word = word.replace(" ", "").lower()
word_forward = word[0::]
word_backward = word[::-1]

if word_forward == word_backward:
    print("This word is a palindrom")
else:
    print("This word isn't a palindrome")


