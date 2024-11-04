# Connor Pavicic, authorizedChecker

auth1 = "1234"
auth2 = "4321"
auth3 = "4231"
auth4 = "7592"
auth5 = "8402"
auth6 = "9999"
auth7 = "0000"
auth8 = "8532"
admin = "1029384756"

while True:
    password = input("What is the password?: ")

    if password == auth1:
        print("Hello authorized user number 1!")
    elif password == auth2:
        print("Hello authorized user number 2")
    elif password == auth3:
        print("Hello authorized user number 3")
    elif password == auth4:
        print("Hello authorized user number 4")
    elif password == auth5:
        print("Hello authorized user number 5")
    elif password == auth6:
        print("Hello authorized user number 6")
    elif password == auth7:
        print("Hello authorized user number 7")
    elif password == auth8:
        print("Hello authorized user number 8")
    elif password == admin:
        print("Hello admin!")
    else:
        print("Password not found.")