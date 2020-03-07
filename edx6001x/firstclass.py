# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:04:14 2020

@author: cerit
"""
import math

class dick(object):
    def __init__(self, length, girth, hasahat):
        self.length = length
        self.girth = girth
        self.hasahat = hasahat

    def __str__(self):
        return '8'+'-'*self.length+'>'

    def get_area(self):
        radius = self.girth / math.tau
        area = (.5) * math.tau * radius**2
        return area

    def get_volume(self):
        area = self.get_area()
        volume = area*self.length
        return volume

    def __eq__(self, other):
        if self.length == other.length and self.girth == other.girth:
            return True
        else:
            return False
        
    def __lt__(self, other):
        if self.length < other.length:
            return True
        else:
            return False