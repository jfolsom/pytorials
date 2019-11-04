# Print Unicode Chart
firstuni = 32    #first character to print
lastuni = 112    #last character to print
perline = 10    #number of characters per line


for i in range(lastuni - firstuni):
    hposition = i % perline
    ipair = str(firstuni + i) + chr(firstuni + i)
    ipair = ipair.ljust(4)
    print(ipair, end='|')
    # start a new line once perline pairs have printed
    ## print('i', i)
    ## print('hposition', hposition)
    if (hposition+1) % perline == 0:
        print('\n')


