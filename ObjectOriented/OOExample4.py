# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:11:45 2018

@author: arpujaha
"""

class MyClass1:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10
    
    def __str__(self):
        return "{}: {}".format(self.name, self.health)

obj = MyClass1("Arta")

#print(obj.health)
print(obj )