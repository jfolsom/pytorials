def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('error: Invalid argument')
print(spam(2))
print(spam(3))
print(spam(20))
print(spam(0))
print(spam(1))

