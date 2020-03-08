# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:28:35 2020

@author: cerit
"""

def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''        
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output