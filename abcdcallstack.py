# Practice with call stack
def a():
    print('a() starts')
    localtest = 'localtest'
    b(localtest)
    d()
    print('a() returns')

def b(localtest):
    localtest = 'localtest'
    print('b() starts', localtest)
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()
