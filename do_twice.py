def do_twice(f, myvalue):
    f(myvalue)
    f(myvalue)

def print_spam():
    print('spam')

do_twice(print_spam(), 'spamyspam')
