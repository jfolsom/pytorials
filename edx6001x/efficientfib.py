# -*- encoding: utf-8 -*-

"""
cerc 02/16/20, calc fibonacci numbers efficiently using
recursion and dictionary memoization
"""

def fibonacci(n, fibodict):
    if n in fibodict:
        ans = fibodict[n]
    else:
        ans = fibonacci(n-1, fibodict) + fibonacci(n-2, fibodict)
    return ans


fibodict = {1:1, 2:2}
print(fibonacci(6, fibodict))
