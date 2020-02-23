# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 08:51:45 2020

@author: cerit
"""

def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if a >= b:
        high = a
        low = b
    else:
        high = b
        low = a
    if low == 0:
        return high
    else:
        return gcd(low, high % low)

        