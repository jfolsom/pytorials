#! python3
# findcontact.py - Search clipboard text for phone numbers and emails.

import re
import pyperclip

text = pyperclip.paste()

# Create regex expression
pnumberregex = re.compile(r'''( 
                                \(?(\d{3})\)?[\s\-\.]?   # 3 numbers, possibly in parens,
                                                      # possibly a space after
                               (\d{3})                  # followed by three numbers   
                               [\-\.\s]?              # possible seperator
                               (\d{4})                  # last four numbers
                               \s*(?:extension|x|e|ext)?\s?\.?(\d{2,5})? # extension
                           )''', re.VERBOSE)
emailregex = re.compile(r'\w*@\w*\.\w{3}')

numbertuple = pnumberregex.findall(text)
# print('numbertuple')
# print(numbertuple)
emaillist = emailregex.findall(text)

numberlist = []


for i in numbertuple:
    thisnumber = i[1] + '.' + i[2] + '.' + i[3]
    if i[4] != '':
        thisnumber += ('x.' + i[4])
    numberlist.append(thisnumber)
# for i in emailtuple:
    # emaillist.append(i[1])

export = ('Phone Numbers:\n')

for i in numberlist:
    export += i
    export += '\n'

export += 'E-mail addresses:\n'

for i in emaillist:
    export += i
    export += '\n'

print(export)

