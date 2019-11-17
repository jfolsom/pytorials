#! python3
# bulletpointadder.py - A program to add bullet points to
# the start of each line in the clipboard

import pyperclip

fromclipboard = pyperclip.paste()
if '\r\n' in fromclipboard:
    userlinebreak = '\r\n'
else:
    userlinebreak = '\n'
listoflines = fromclipboard.split(userlinebreak)

bulletedlist = []



for i in range(len(listoflines)):
    appendthis = '* ' +  listoflines[i] + '\n'
    bulletedlist.append( "* " + listoflines[i] + '\n')



bulletedlist = ''.join(bulletedlist)

pyperclip.copy(bulletedlist)
