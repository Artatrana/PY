# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:30:38 2018

@author: arpujaha
"""

class Person:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        other_guy.health = other_guy.health - self.damage


art = Person("Arta")
you = Person("Mita")

print(art.name)
print(you.name)

print(you.attack(art))
print(art.health)