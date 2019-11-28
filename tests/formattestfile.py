#! Python3
# formattestfile.py - Take a user friendlyish formatted test file and convert
# to an format easier for python to use.


import os
import sys
import re
import time
import pprint



def validatefile(fileobject):
    # run some checks to find out if that a fileobject matches a correctly
    # formated test file
    filestring = fileobject.read()
    
    # Abort if the file is  does not match this heuristic for plaintext.
    hastextregex = re.compile(r'\s\w{3,15}\s')
    hastextmo = hastextregex.search(filestring)
    if hastextmo == None:
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
    val_file_sectionregex = re.compile(r'(?:\n|\r\n|\r)SECTION, ')
    if val_section_regex.search(filestring) == None:
        print('Input file has no lines starting with CA; aboring.')
        time.sleep(2)
        sys.exit()
    
    # If there are more question then correct answers, abort.
    if len(ca_regex.findall(filestring)) < len(qqregex.findall(filestring)):
        print('There are more questions then correct answers; aborting.')
        time.sleep(2)
        sys.exit()
    
    # If there are duplicate section headers, abort.
    val_sectionregex = re.compile(r'SECTION,\w.*(?:\n|\r\n|\r){2}')
    foundbreaks = val_sectionregex.findall(filestring)
    if len(foundbreaks) != len(set(foundbreaks)):
        print('You appear to have duplicate section names; aborting.')
        time.sleep(2)
        sys.exit


def stringtosections(longstring, listofsectionbreaks)
    # Search long string for a list of section breaks.  List of
    # breaks will frequently come from a regex.findall(longstring).  Return the
    # a list of strings containing each sections contents.  DOES NOT keep
    # section names.
    # v0.0.1 JF 2019-11-28 Not yet checked.
    stringremainder = longstring
    listofsections = ['']
    for sectionbreak in listofsectionbreaks:
        # For each substring in the list provided, first, find where it starts and
        # mark that position.
        startcutat = stringremainder.index(sectionbreak)
        # Then figure out where the substring stops 
        lengthofcutis = len(sectionbreak)
        endcutat = startcutat + lengthofcutis
        # Add the section to the list, then chop off the first section and
        # the sectionbreak from the longstring.
        listofsections.append(stringremainder[:startcutat])
        stringremainder = stringremainder[endcutat:])
    return listofsections
        
        
# The main sequence begins here.
# First, check the provided filepath and make sure it points at a valid file.
userformatpath = sys.argv[1]
if not os.path.isfile(userformatpath):
    print('''Enter a valid file path e.g. "questions.txt" or
    "C:\\users\\cerit\\tests\\automatteste\\questions.txt" as a paramater
    when invoking this program. If the file path contains folder names with
    spaces, you must enclose the path in double quotes. Aborting.''')
    time.sleep(2)
    sys.exit()

# Now, open it and assign its contents to a string variable.
userfileobject = open(userformatpath)
validatefile(userfileobject)
print('User input file validation passed (but the process isn\'t\n' +
       'all that stringent)')
time.sleep(1)
userfilestring = read(userfileobject)

# Split that string into a list of sections
sectionregex = re.compile(r'SECTION,\w.*(?:\n|\r\n|\r){2}')
foundbreaks = sectionregex.findall(userfilestring)
sections = stringtosections(userfilestring, foundbreaks)
pprint.pprint(sections)
# Had to stop codeing here, havent't tested.  Next step, test program to here.

    
    
