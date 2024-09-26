question_1 = int(input("What is 2+2?: "))
question_2 = int(input("What is 9 + 10?: "))
question_3 = int(input("How many fingers do you have?: "))
question_4 = int(input("What is 2 raised to the 3rd power?: "))
question_5 = int(input("what is 5 factorial?: "))
score = 5

if question_1 == 4:
    score = score
else:
    score = score-1

if question_2 == 19:
    score = score
else:
    score = score-1

if question_3 == 5:
    score = score
else:
    score = score-1

if question_4 == 8:
    score = score
else:
    score = score-1

if question_5 == 120:
    score = score
else:
    score = score-1

print("You got a",score,"/5")