# Connor Pavicic, countdown

import time

amount = int(input("How many seconds do you want to set the timer to?: "))
print(amount)
time.sleep(1)

while amount > 0:
    amount -= 1
    print(amount)
    time.sleep(1)