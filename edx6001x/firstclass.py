# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:04:14 2020

@author: cerit
"""
import math
import random

class dick(object):
    def __init__(self, length, girth, hasahat):
        self.length = length
        self.girth = girth
        self.hasahat = hasahat

    def getlength(self):
        return self.length

    def getgirth(self):
        return self.girth

    def gethasahat(self):
        return self.hasahat

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


class Animal(object):
    def __init__(self, age=0):
        self.age = age
        self.name = None

    def getage(self):
        return self.age

    def getname(self):
        return self.name

    def setage(self, newage):
        self.age = newage

    def setname(self, newname=''):
        self.name = newname

    def __str__(self):
        return('animal:%s:%s' % (self.name, self.age))


class Cat(Animal):
    def speak(self):
        print('meow')

    def __str__(self):
        return('cat:%s:%s' % (self.name, self.age))


class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def getrid(self):
        return str(self.rid).zfill(3)

    def getparent1(self):
        return self.parent1

    def getparent2(self):
        return self.parent2
    
    def speak(self):
        print('meep')

    def __str__(self):
        return('rabbit:%s:%s' % (self.name, self.age))

    def __add__(self, other):
        return Rabbit(0, self, other)
    
    def __eq__(self, other):
        #if both rabbits have the same parents, then they are 'equal'
        parent1same = self.parent1.getrid() == other.parent1.getrid()
        parent2same = self.parent2.getrid() == other.parent2.getrid()
        p1eqp2 = self.parent1.getrid() == other.parent2.getrid()
        p2eqp1 = self.parent2.getrid() == other.parent1.getrid()
        return (parent1same and parent2same) or (p1eqp2 and p2eqp1)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.name = name
        self.friends = []

    def getfriends(self):
        return self.friends

    def setfriends(self, newfriends):
        self.friends = newfriends

    def age_diff(self, other):
        diff = self.age - other.age
        if diff >= 0:
            print('%s is %s years older than %s' %
                  (self.name, diff, other.name))
        else:
            print('%s is %s years younger than %s' %
                  (self.name, -1*diff, other.name))

    def speak(self):
        print('hello')

    def __str__(self):
        return('person:%s:%s' % (self.name, self.age))


class Student(Person):
    def __init__(self, name, age, major='undeclared'):
        Person.__init__(self, name, age)
        self.major = major

    def change_major(self, newmajor):
        self.major = newmajor

    def speak(self):
        r = random.choice(['I have homework.',
                           'I need sleep.',
                           'I should eat.',
                           'I am watching TV.'])
        print(r)

    def __str__(self):
        return('student:%s:%s' % (self.name, self.age))
    
    def __lt__(self, other):
        return self.id < other.id




