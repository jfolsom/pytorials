# Perform the Collatz sequence on user's integer
# until the value displayed is 1.
# Display each value.
import sys
import time

def receive_integer():
    print('Enter a positive integer:')
    receivednumber = 'dummy'
    while receivednumber == 'dummy':
        try:
            receivednumber = int(float(input()))
            if not receivednumber > 0:
                print('That number is not positive.')
                continue
        except ValueError:
            print('That is not an integer.')
            continue
    print('Success:', receivednumber)
    return receivednumber

def collatz(collatznumber):
    if (collatznumber % 2) == 0:   #is even
        collatznumber = collatznumber // 2
    elif (collatznumber % 2) == 1: #is odd
        collatznumber = collatznumber*3 + 1
    else:
        print('How did we get here? 01')
    return collatznumber

def outputloop():
    number = receive_integer()
    while number != 1:
        print(number)
        number = collatz(number)
        time.sleep(0.3)
    if number == 1:
        print(number)
    else:
        print('How did we get here? 02')

outputloop()


