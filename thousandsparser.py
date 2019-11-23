#! Python3

import re

text = """
Sample      PSF
B-1         23452
B-2         800
B-3         1234569
"""

print('Original text:')
print(text)

thousandsregex = re.compile(r'\s(\d{1,3})(\d{3})?(\d{3})?(\d{3})\s')

fourplusdigits = thousandsregex.findall(text)

print('fourplusdigits')
print(fourplusdigits)

for numbertuple in fourplusdigits:
    print('numbertuple')
    print(numbertuple)
    numberfound = ''
    formattednumber = ''
    for group in numbertuple:
        numberfound += group
        formattednumber += group
        if (group != numbertuple[-1]) and group != '':
            formattednumber +=','
    start = text.index(numberfound)
    print('start')
    print(start)
    print('numberfound')
    print(numberfound)
    print('formattednumber')
    print(formattednumber)
    print('---nextiter---')
    text = text[0:start] + formattednumber +text[(start+len(numberfound)):len(text)]

print('Finished text')
print(text)