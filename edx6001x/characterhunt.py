# -*- coding: utf-8 -*-

"""
input: a single character, then string in alphabatized order
returns True if the character is in the string
"""

debug = True

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if debug is True: print('entering is in.  char:', char, 'aStr:', aStr)
    if debug is True: print('len(aStr)', len(aStr), 'len//2', len(aStr)//2)
    if debug is True: print('aStr[len(aStr)//2:]', aStr[len(aStr)//2:])
    if debug is True: print('aStr[:len(aStr)//2]', aStr[:len(aStr)//2])
    if char == aStr:
        return True
    elif len(aStr) == 0:
        return False
    elif len(aStr) == 1 and aStr != char:
        return False
    elif ord(aStr[len(aStr)//2]) == ord(char):
        return True
    elif ord(aStr[len(aStr)//2]) > ord(char):
        # if the character in the middle of aStr is later in the alphabet then
        # the character we are seaching for, then let's look in the first half
        # of aStr
        return isIn(char, aStr[:len(aStr)//2])
    elif ord(aStr[len(aStr)//2]) < ord(char):
        # if the character in the middle of aStr is later in the alphabet then
        # the character we are seaching for, then let's look in the second half
        # of aStr
        return isIn(char, aStr[len(aStr)//2:])
        
aStr = input('a string :')
char = input('a char :')
print(isIn(char, aStr))