# Connor Pavicic, gradeChecker

num_of_grades = int(input("How many grades do you want to check?: "))

A = range(90, 101)
B = range(80, 90)
C = range(70, 80)
D = range(60, 70)

num = 0

while num < num_of_grades:
    grade = int(input("What percentage is your grade?: "))
    if grade in A:
        print("Nice, you have an A!")
        num += 1
    elif grade in B:
        print("Nice, you have a B!")
        num += 1
    elif grade in C:
        print("You have a C, keep trying.")
        num += 1
    elif grade in D:
        print("You have a D, do better.")
        num += 1
    else:
        print("You have an F. Lock in man.")
        num += 1