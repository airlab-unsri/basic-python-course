# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:11:36 2019

@author: DELL
"""

class Parrot :
    def fly(self):
        print("Parrot can fly ")
    def swim (self):
        print("Parrot can't Swim")
class Penguin:
    def fly(self):
        print("Penguin can't fly")
    def swim(self):
        print("Penguin can swim")
        
#Common Interface
def flying_test(bird):
    bird.fly()
    
#instance object
blu=Parrot()
peggy=Penguin()
#passing the object
flying_test(blu)
flying_test(peggy)