print('mywordslen = ')
mywordslen = int(input())
mywords = []
mystring = ''
for i in range(mywordslen):
    print('Enter item', i)
    mywords.append(input())
print(mywords)

for index in range(len(mywords)-1):
    mywords[index] += ', '

try:
    mywords[len(mywords)-1] +='.'
except IndexError:
    foo = 1



for index, item in enumerate(mywords):
    mystring += item

print(mystring)

print(mystring)

