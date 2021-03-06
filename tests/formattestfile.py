#! Python3
# formattestfile.py - Take a user friendlyish formatted test file and convert
# to an format easier for python to use.


import os
import sys
import re
import time
import pprint



def validatefilestring(filestring):
    # run some checks to find out if that a string matches a correctly
    # formated test file
    # Abort if the file is  does not match this heuristic for plaintext.
    hastextregex = re.compile(r'\s\w{3,15}\s')
    hastextmo = hastextregex.search(filestring)
    if hastextmo == None:
        print('hastextmo:')
        print(hastextmo)
        print('hastextmo.group():')
        print(hastextmo.group())
        print('Input file does not appear to be plaintext, because it' +
              'doesn\'t have a word between three and fifteen characters' +
              'surrounded by spaces; aborting.')
        time.sleep(2)
        sys.exit()
    
    # Abort if the file doesn't contain a properly formatted question line.
    qqregex = re.compile('QQ')
    if qqregex.search(filestring) == None:
        print('Input file has no lines starting with QQ; aboring.')
        time.sleep(2)
        sys.exit()
    
    # Abort if the file doen't contain a properly formatted answer line.
    ca_regex = re.compile('CA')
    if ca_regex.search(filestring) == None:
        print('Input file has no lines starting with CA; aboring.')
        time.sleep(2)
        sys.exit()
    
    # Abort if the file doen't contain a properly formatted section header.
    val_sectionregex = re.compile(r'(?:\n|\r|\r\n)SECTION,\s.*(?:\n|\r|\r\n)')
    if val_sectionregex.search(filestring) == None:
        print('Input file has no lines starting with CA; aboring.')
        time.sleep(2)
        sys.exit()
    
    # If there are more question then correct answers, abort.
    if len(ca_regex.findall(filestring)) < len(qqregex.findall(filestring)):
        print('There are more questions then correct answers; aborting.')
        time.sleep(2)
        sys.exit()
    
    # If there are duplicate section headers, abort.
    sectiontitlesregex = re.compile(r'^"SECTION,\w.*(?:\n|\r\n|\r){2}')
    foundbreaks = sectiontitlesregex.findall(filestring)
    if len(foundbreaks) != len(set(foundbreaks)):
        print('You appear to have duplicate section names; aborting.')
        time.sleep(2)
        sys.exit


def stringtosections(longstring, listofsectionbreaks):
    # Search long string for a list of section breaks.  List of
    # breaks will frequently come from a regex.findall(longstring).  Return the
    # a list of strings containing each sections contents.  DOES NOT keep
    # section names.
    # v0.0.1 JF 2019-11-28 Not yet checked.
    stringremainder = longstring
    listofsections = []
    for i in range(len(listofsectionbreaks)-1):
        # For each sectionbreak provided, except the last:
        # Mark the postion of this seciton break and the next section break
        thissectionbreak = listofsectionbreaks[i]
        nextsectionbreak = listofsectionbreaks[i+1]
        sectionstart = stringremainder.index(thissectionbreak)
        sectionend = stringremainder.index(nextsectionbreak)
        # Add the section to the list, then chop it off the string
        listofsections.append(stringremainder[sectionstart:sectionend])
        stringremainder = stringremainder[sectionend:]
    # Add the reminder as the last section
    listofsections.append(stringremainder)
    return listofsections
        
        
# The main sequence begins here.
# First, check the provided filepath and make sure it points at a valid file.
userformatpath = sys.argv[1]
print('userformatpath:')
print(userformatpath)
if not os.path.isfile(userformatpath):
    print('''Enter a valid file path e.g. "questions.txt" or
    "C:\\users\\cerit\\tests\\automatteste\\questions.txt" as a paramater
    when invoking this program. If the file path contains folder names with
    spaces, you must enclose the path in double quotes. Aborting.''')
    time.sleep(2)
    sys.exit()

# Now, open it and assign its contents to a string variable.
userfileobject = open(userformatpath)
print('userfileobject:')
print(userfileobject)
userfilestring = userfileobject.read()
print('userfilestring')
print(userfilestring)
validatefilestring(userfilestring)
print('User input file validation passed (but the process isn\'t\n' +
       'all that stringent)')
time.sleep(1)

# Split that string into a list of sections
sectionregex = re.compile(r'(?:\n|\r|\r\n)SECTION,\s(.*)(?:\n|\r|\r\n)')
foundbreaks = sectionregex.findall(userfilestring)
print('foundbreaks')
print(foundbreaks)
sections = stringtosections(userfilestring, foundbreaks)
print('sections:')
for i in range(len(sections)):
    print(i)
    print(sections[i])
userfileobject.close()

    
    
