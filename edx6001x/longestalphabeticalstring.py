# Python3
"""
Created on Sun Jan 26 18:31:56 2020

@author: Jacob Folsom
"""

# Find the longest string where each successive letter is alphabetical
# Same letter twice counts as alphabetical.
# Assume all supplied letters are lowercase, no spaces.

s = 'zyxwvu'

lengthofs = len(s)
highscore = 1
hs_position = 0
debug = False

def alphorderpair(twoletterstring):
    # See if the second letter is alphabetically earlier then the first)
    # Only works on all lower case english letters
    # Returns true if in alphabetical order or same letter twice,
    # False if not
    if len(twoletterstring) != 2 or not isinstance(twoletterstring, str):
        print('must pass alphaorderpair a two letter string', end=';')
    if ord(twoletterstring[0]) <= ord(twoletterstring[1]):
        if debug == True: print('aopair returning True', end=';')
        return(True)
    else:
        if debug == True: print('aopair returning False', end=';')
        return(False)


def alphorderchunk(chunk):
    # Check the string to see if its in alphabetical order
    if debug == True: print('--begin alphorderchunk--')
    for position in range(len(chunk)- 1):
        if debug == True: print('pos within alphorderchunk', position, end=';')
        pair = chunk[position:position+2]
        if debug == True: print('about to pass pair "'+pair+'"', end=';')
        if not alphorderpair(pair):
            if debug == True: print('--alphorderchunk returning False--')
            return False
    if debug == True: print('--alphorderchunk returning True--')
    return True
            
        
for startpos in range(lengthofs-1):
    if debug == True: print('*********')
    if debug == True: print('startpos:', startpos, ', ', s[startpos])
    failedtest = False
    for chunklength in range(2, 1 + lengthofs - startpos, 1):
        chunk = s[startpos:startpos+chunklength]
        if debug == True: print('chunklength :', chunklength)
        if debug == True: print('chunk: ', chunk)
        if debug == True: print('alphorderchunk:', alphorderchunk(chunk))
        if alphorderchunk(chunk):
            if chunklength > highscore:
                highscore = chunklength
                hs_position = startpos
                if debug == True: print('A high score is earned by:', end='')
                if debug == True: print(chunk)
                if debug == True: print('!!!!!!!!!!!New highscore:', end='')
                if debug == True: print(chunklength -1, 'at pos', startpos)
        else:
            if debug == True: print('failed alphaorderchunk, so break')
            break

chickendinner = s[hs_position : hs_position+highscore]
print('Longest substring in alphabetical order is:', chickendinner)        