# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:36:28 2020

@author: cerit
"""

class Pencil(object):
    def __init__(self, leadthickness, color, mechanical):
        self.leadthickness = leadthickness
        self.color = color
        self.mechanical = mechanical

    def getleadthickness(self):
        return self.leadthickness

    def setleadthickness(self, leadthickness):
        self.leadthickness = leadthickness

    def getcolor(self):
        return self.color

    def setcolor(self, color):
        self.color = color

    def getmechanical(self):
        return self.mechanical

    def setmechanical(self, mechanical):
        self.mechanical = mechanical