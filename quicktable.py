#! sort table data

import sys

tabledata = [['animals', 'dog', 'cat', 'haloquadratum'],
             ['vegetables', 'le carrort', 'le pomme de terre', 'le salad'],
             ['Swedish Monarchs', 'Eric Segersall', 'Olof Skotkonung', ' Anund Jacob']]

# print(tabledata)

# find the longest word in each column
def longest(yourtable):
    # print warning and break if table is not a list or ...
    rows = len(yourtable[0])
    columns = len(yourtable)    
    if type(yourtable) is not list:
        print('empty list')
        sys.exit()
    # ... if it is not a square list
    for i in range(columns):
        if not len(yourtable[i]) == rows:
            print('row', i, 'does not have', rows, 'rows')
            sys.exit()
       
    # make a list of the length of the longest word in each column
    wordwidths = []
    for x in range(columns):
        longword = 0
        for y in range(rows):
            if len(yourtable[x][y]) > longword:
                longword = len(yourtable[x][y])
        wordwidths.append(longword)
    return wordwidths
wordwidths2 = longest(tabledata)

# rjustify each column so that each item is equal to the longest characters + 2
thisfar = 0
rows = len(tabledata[0])
columns = len(tabledata)
for i in range(columns):
    thisfar = wordwidths2[i] + 2
    for j in range(rows):
        tabledata[i][j] = tabledata[i][j].rjust(thisfar)

for y in range(rows):
    for x in range(columns):
        print(tabledata[x][y], end='')
    print('\n')