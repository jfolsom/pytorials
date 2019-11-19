#! python - Search clipboard text for phone numbers and emails.

import re
import pyperclip

text = pyperclip.paste()

pnumberregex = re.compile(r'''
                                \d{3}           # followed by 3 digits
                                (\s|\.|-)?      # optional separator
                                \d{3}           # followed by 3 digits
                                (\s|\.|-)?      # optional separator
                                \d{4}           # followed by 4 digits
                                (\s*(ext|x|x\.|ext\.)\s*\d{2,5})?  # optional extension
                             ''', re.VERBOSE)
emailregex = re.compile(r'\w*@\w*\.\w{3}')

numbertuple = pnumberregex.findall(text)
print('numbertuple')
print(numbertuple)
emaillist = emailregex.findall(text)

numberlist = []


for i in numbertuple:
    numberlist.append(i[0])

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
