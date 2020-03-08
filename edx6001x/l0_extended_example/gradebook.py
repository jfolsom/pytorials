# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:30:52 2020

@author: cerit
"""
import random

class Grades(object):
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True

    def getstudents(self):
        return self.students

    def addstudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def getgrades(self, student):
        try:
            return self.grades[student.getIdNum()]
        except KeyError:
            raise ValueError('Student not in grade book')

    def addgrade(self, student, grade):
        """ Assumes: grade is a float
            Add grade to the list of grades for student."""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        """Return a alist of a all the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]

class Student(object):
    nextIdNum = 0
    def __init__(self, name):
        self.name = name
        self.IdNum = Student.nextIdNum
        Student.nextIdNum += 1

    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name
    
    def getIdNum(self):
        return self.IdNum
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __str__:
    
testclass = Grades()
alf = Student('Alf')
benny = Student('Benny')
carl = Student('Carl')
testclass.addstudent(alf)
testclass.addstudent(benny)
testclass.addstudent(carl)
testclass.addgrade(carl, round(random.random()*100, 2))
testclass.addgrade(alf, round(random.random()*100, 2))
testclass.addgrade(benny, round(random.random()*100, 2))
testclass.addgrade(benny, round(random.random()*100, 2))
testclass.addgrade(alf, round(random.random()*100, 2))
testclass.addgrade(alf, round(random.random()*100, 2))
testclass.addgrade(alf, round(random.random()*100, 2))
testclass.addgrade(alf, round(random.random()*100, 2))
