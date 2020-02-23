# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:55:01 2020

@author: cerit
"""

low = 0
high = 100
guess = 50
print('Please think of a number between 0 and 100!')

while 1 == 1:
    print('Is your secret number '+str(guess)+'?')
    response = input("Enter 'h' to indicate the guess is too high. " +
                     "Enter 'l' to indicate the guess is too low. " +
                     "Enter 'c' to indicate I guessed correctly. ")
    if response == 'l':
        low = guess
    elif response == 'h':
        high = guess
    elif response == 'c':
        break
    else: print('Sorry, I did not understand your input.')
    guess = (low + high) // 2

print('Game over. Your secret number was:', guess)        