# Connor Pavicic, Histogram

amount = int(input('How many numbers do you want to do: '))
count = 0

while count<amount:
    num = int(input('Enter a number: '))
    output = ''
    for x in range(num):
        output += '*'
    print(num, ':', output)
    count += 1