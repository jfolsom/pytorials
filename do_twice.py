def do_twice(f, myvalue):
    f(myvalue)
    f(myvalue)

def print_twice(arg):
    print(arg)
    print(arg)

do_twice(print_twice, 'spamyspam')
