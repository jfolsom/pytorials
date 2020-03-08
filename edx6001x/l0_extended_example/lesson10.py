# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:01:42 2020

@author: Jacob folsom
"""
import datetime


class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastname = name.split(' ')[-1]

    def getname(self):
        return self.name

    def getlastname(self):
        return self.lastname

    def setname(self, name):
        self.name = name

    def getbirthday(self):
        return self.birthday

    def setbirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

    def getage(self):
        """ returns the self's current age IN *DAYS* """
        if self.birthday is None:
            raise ValueError('asked for age but never provided birthday')
        else:
            return (datetime.date.today() - self.birthday).days

    def __str__(self):
        return self.name

    def __lt__(self, other):
        """ returns True if self is lexicaographically less than other's name.
        """
        return self.lastname[1] < other.lastname[1]
        if self.lastname == other.lastname:
            return self.name < other.name
        else:
            return self.lastname < other.lastname

class MITPerson(Person):
    
    nextid = 1

    def __init__(self, name):
        Person.__init__(self, name)
        self.id = MITPerson.nextid
        MITPerson.nextid += 1

    def getid(self):
        return self.id

    def speak(self, utterance):
        return (self.getlastname() + ' says: ' + utterance)

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classyear):
        MITPerson.__init__(self, name)
        self.year = classyear

    def getyear(self):
        return self.getyear

    def speak(self, utterance):
        return MITPerson.speak(self, ' Dude, ' + utterance)


class TransferStudent(Student):
    pass


class GradStudent(Student):
    pass


def isstudent(obj):
    return isinstance(obj, Student)


class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def getdepartment(self):
        return self.department

    def setdepartment(self, department):
        self.department = department

    def speak(self, utterance):
        return MITPerson.speak(self, 'In course ' + self.department +
                               ' we say ' + utterance)

    def lecture(self, topic):
        return self.speak('It is obvious that ' + topic)


a = UG('Ted Nugent', 1980)
b = UG('Bob Woodward', 1982)
c = UG('Bob Dylan', 1970)
admin = MITPerson('Stevedave')
d = GradStudent('Mahatma Ghandi')
e = TransferStudent('Alien Al')
EricGrimson = Professor('Eric Grimson', 'CS')
