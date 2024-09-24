# Connor Pavicic, Fibonacci
import time

x = 1
y = 0

while True:
    final_num = x+y
    print(final_num)
    y = x
    x = final_num
    time.sleep(0.5)