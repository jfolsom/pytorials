# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:47:43 2020

@author: Jacob Folsom
"""
# Find a root of a 2nd order equation using the Newton-Raphson Method
# equation of the form Ax^2 + Bx + C.


try:
    debug == False
except NameError:
    debug = False


def polyf(x, A, B, C):
    return A*x**2 + B*x + C


def polyfprime(x, A, B):
    return 2*A*x + B


def raphson2nd(A, B, C, epsilon):
    guess = 0
    numberguesses = 0
    while abs(polyf(guess, A, B, C) - 0) >= epsilon:
        if debug == True: print('\n', 'entering loop w/ guess:',guess, end=';')
        f = polyf(guess, A, B, C)
        if debug == True: print('f(guess)=', f, end=';')
        fprime = polyfprime(guess, A, B)
        if debug == True: print('fprime:', fprime, end=';')
        guess = guess - (f/fprime)
        if debug == True: print('leaving loop with new guess:', guess, '---')
        numberguesses += 1
    return guess, numberguesses


if __name__ == '__main__':
    A = 1
    B = 3
    C = -28
    epsilon = 2**-16

    raphsonroot, raphsonguesses = raphson2nd(A, B, C, epsilon)

    print('number of guesses for raphson:', raphsonguesses)
    print(raphsonroot, 'is an approx. root of ', end='')
    print(str(A)+'x^2 + '+str(B)+'x + '+str(C))
