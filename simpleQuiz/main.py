# Connor Pavicic, simpleQuiz

score = 0
question_count = 0
question_1 = float(input("""What is the log of 2 (Round to the nearest tenth.)
                       A. 0.3
                       B. 1.3
                       C. 2.3
                       D. 3.3
                    
                       Answer: """))
if question_1 == 0.3:
    print('Correct!')
    score += 1
    question_count += 1
else:
    easy_question2 = int(input("What is 2+2?"))