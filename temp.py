debug = True
aTup = ('fred', 'ed', 0, 999, (1, 2))

def oddTuples(aTup):
    newtup = ()
    for count, item in enumerate(aTup):
        if item%2 == 0:
            newtup = newtup + item
    return newtup
    
print(oddTuples(aTup))
print(oddTuples(aTup))