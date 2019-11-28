#! Python3
# Kilroy a file

import os
import sys
import re

target = sys.argv[1]
endoflineregex = re.compile(r'\n$|\r$|\r\n$')

if not os.path.isfile(target):
    print('Pass a valid file path as an argument')
    sys.exit()
    
myfile = open(target)
lines = myfile.readlines()
myfile.close()


# If the last line doesn't end with newline, add one.
#   First, what are the normal line endings for this file, just in case.
firstlineendingmo = endoflineregex.search(lines[0])
if firstlineendingmo == None:
    lineend = '\n'
else:
    lineend = firstlineendingmo.group()

lastlinemo = endoflineregex.search(lines[-1])
myfile = open(target, 'a')
if lastlinemo == None:
        myfile.write(lineend)
    
myfile.write('a')
myfile.write('Killroy was here')
myfile.close()
    
    
    
    