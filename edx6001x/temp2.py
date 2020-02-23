# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:45:54 2020

@author: cerit
"""

def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)

print(factorial(5))