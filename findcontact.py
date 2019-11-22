#! python - Search clipboard text for phone numbers and emails.

import re
import pyperclip

text = pyperclip.paste()

pnumberregex = re.compile(r''' \d{3}                #three digits
                           ''', re.VERBOSE)
emailregex = re.compile(r'\w*@\w*\.\w{3}')

numberlist = pnumberregex.findall(text)
print('numberlist')
print(numberlist)
emaillist = emailregex.findall(text)

# numberlist = []


# for i in numbertuple:
    # numberlist.append(i[0])

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
