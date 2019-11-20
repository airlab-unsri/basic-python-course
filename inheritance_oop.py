# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:36:14 2019

@author: DELL
"""
#Parent class

class bird:
    def  __init__(self):
        print("Bird Is ready ")
        
    def whoisthis (self):
        print("Bird")
        
    def swim(self):
        print("Swim Faster")
        
#Child Class
        
class Penguin(bird):
    def  __init__ (self):
        super(). __init__()
        print("Penguin is Ready")
        
    def whoisthis(self):
        print("Penguin")
        
    def run(self):
        print("Run Faster")

imam=Penguin()
imam.whoisthis()
imam.swim()
imam.run()
    