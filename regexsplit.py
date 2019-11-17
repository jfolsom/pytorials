# Write your code here :-)
import re
mystring = 'a\nbcd\refgh\nijk'
print('mystring:')
print(mystring)
splitlist = re.split('\n|\r', mystring)
print('splitlist')
print(splitlist)
for i in splitlist:
    print(i)


