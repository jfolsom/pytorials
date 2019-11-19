mystring = '12'
mylist = [1, 2]
mytuple = (1, 2)

def add3string(somestring):
    somestring += '3'
    print('somestring')
    print(somestring)
    
def add3list(somelist):
    somelist += [3]
    print('somelist')
    print(somelist)

def add3tuple(sometuple):
    sometuple += (3,)
    print('sometuple')
    print(sometuple)

add3string(mystring)
add3list(mylist)
add3tuple(mytuple)

print('mystring')
print(mystring)
print('mylist')
print(mylist)
print('mytuple')
print(mytuple)