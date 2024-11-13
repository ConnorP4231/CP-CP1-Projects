# Connor Pavicic, simpleQuiz

score = 0
question_count = 0
question_1 = input("""What is the log of 2 (Round to the nearest tenth.)
A. 0.3
B. 1.3
C. 2.3
D. 3.3
                    
Answer: """)
question_count += 1

if question_1 == '0.3' or question_1 == 'A':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    question_count += 1
    easy_question1 = int(input("""What is 2+2?
A. 2
B. 3
C. 4
D. 5
                               
 Answer: """))
    if easy_question1 == '4' or easy_question1 == 'C':
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
    
question_2 = input("""Spell red:
                   
A. lster
B. red
C. der
D. All of the above
                   
Answer: """)
question_count += 1

if question_2 == 'red' or question_2 == 'B':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    question_count += 1
    easy_question2 = input("""What is the first letter of the alphabet?
A. C
B. D
C. A
D. B
                           
Answer: """)
    if easy_question2 == 'A' or easy_question2 == 'C':
        print('Correct!')
        score += 1
        if question_count >= 5:
            print('You have answered 5 questions and your score is', score, '/5')
            quit()
    else:
        print('Incorrect!')
        if question_count >= 5:
            print('You have answered 5 questions and your score is', score, '/5')
            quit()

question_3 = input("""What is the square root of 9 squared?: 
A. 3
B. 6
C. 9
D. 12
                   
Answer:""")
question_count += 1

if question_3 == '9' or question_3 == 'C':
    score += 1
    print('Correct!')
    if question_count >= 5:
        print('You have answered 5 questions and your score is', score, '/5')
        quit()
else:
    print('Incorrect ')
    if question_count >= 5:
        print('You have answered 5 questions and your score is', score, '/5')
        quit()
    easy_question3 = input("""How many letters are in this question
A. 28
B. 29
C. 30
D. 31
                           
Answer: """)
    question_count += 1

    if easy_question3 == 'D' or easy_question3 == '31':
        print('Correct!')
        score += 1
        if question_count >= 5:
            print('You have answered 5 questions and your score is', score, '5')
            quit()
    else:
        print('Incorrect')
        if question_count >= 5:
            print('You have answered 5 questions and your score is', score, '/5')
            quit()

question_4 = input("""The answer is D. 3
A. 0
B. 1
C. 2
D. 3
                   
Answer: """)
question_count += 1

if question_4 == 'D' or question_4 == '3':
    print('Correct!')
    score += 1
    if question_count >= 5:
        print('You have answered 5 questions and your score is', score, '/5')
        quit()
else:
    print('You are a failure, how do you get that wrong.')
    easy_question4 = input("""How do you say Hello in English?
A. H
B. Hello
C. A
D. FitnessGram™ Pacer Testi, ilerledikçe giderek zorlaşan çok aşamalı bir aerobik kapasite testidir.
20 metre tempo testi 30 saniye içinde başlayacak. Başlangıçta sıraya girin.
Koşu hızı yavaş başlar ancak bu sinyali duyduktan sonra her dakika daha da hızlanır.""")
    question_count += 1
    
    if easy_question4 == 'B' or easy_question4 == 'Hello':
        print('Correct!')
        score += 1
        if question_count >= 5:
            print('You have answered 5 questions and your score is', score, '/5')
            quit()
    else:
        print('Incorrect')
        if question_count >= 5:
            print('You have answered 5 questions and your score is', score, '/5')
            quit()

question_5 = input("""When is Christmas?
A. December 25
B. February 31
C. December 32
D. Yes""")

if question_5 == 'A' or question_5 == 'December 25':
    print('Correct!')
    score += 1
    if question_count >= 5:
        print('You have answered 5 questions and your score is', score, '/5')
        quit()
else:
    print('Incorrect')
    if question_count >= 5:
        print('You have answered 5 questions and your score is', score, '/5')
        quit()