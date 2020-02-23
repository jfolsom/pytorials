# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

debug = false
import re



def recurucer(aba):
    """
    input string aba
    return True if palindrome (not counting space and punct), else False
    """
    notWregex = re.compile(r"[\W_]")
    aba = notWregex.sub('', aba)
    aba = aba.lower()
    i = 0
    if debug is True: print('recurucer is about to call recer, aba is', aba)
    def recer(aba, i):
        if debug is True: print('entering recer')
        if debug is True: print('ok, now recer just set i to', i)
        if aba == '':
            if debug is True: print('found aba == ""')
            return True
        else:
            return aba[0] == aba[-1] and recer(aba[1:-1], i+1)
    return(recer(aba, i))        
            

aba = input('gimme some')





print(recurucer(aba))