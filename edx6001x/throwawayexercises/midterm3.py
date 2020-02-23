def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    debug = False
    result = 1
    results = [result]
    result = result * base
    results.append(result)
    while result < num:
        result = result * base
        results.append(result)
    if debug == True:
        print('results: ', results)
        print('results[-2]', results[-2], 'results[-1]', results[-1])
        print('abs(results[-2] - num)', abs(results[-2] - num), 'abs(results[-1] - num)', abs(results[-1] - num))
    if abs(results[-2] - num) <= abs(results[-1] - num):
        return len(results) - 2
    else:
        return len(results) - 1

ans = closest_power(2, 4)
print(ans)
