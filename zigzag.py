import time
import sys
indent = 0 # How many spaces to indent
indentincreasing = True # Whether the indentation is increasing or not


try:
    while True:
        print(' ' *indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second

        if indentincreasing:
            indent = indent + 1
            if indent == 20:
                indentincreasing = False
        elif not indentincreasing:
            indent = indent -1
            if indent == 0:
                indentincreasing = True
        else:
            print('How did we get here? 01')
except KeyboardInterrupt:
        sys.exit()

