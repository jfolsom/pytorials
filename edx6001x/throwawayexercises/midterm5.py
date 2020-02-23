def isunique(thisvalue, aDict):
    count = 0
    for value in aDict.values():
        if value == thisvalue:
            count += 1
    if count == 1:
        return True
    else:
        return False


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    for every unique integer item in aDict, return
    the corresponding keys in order
    '''
    returnkeys = []
    for k, v in aDict.items():
        if type(v) == int and isunique(v, aDict):
            returnkeys.append(k)
        try:
            returnkeys.sort()
        except:
            donothing = None
    return returnkeys

aDict = {'g': 23125, 'b': 42, 'c': 223, 'frangible': -23, 'bu': 543, 5: 2, 'bubu': 543, 3: 1, 'carrot': 2}
listylist = uniqueValues(aDict)
print(listylist)
