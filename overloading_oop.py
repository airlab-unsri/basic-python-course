# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:04:01 2019

@author: DELL
"""

class A:
    def  __init__ (self,a):
        self.a =a
    # adding two Object
    def __add__(self,o):
        return self.a + o.a
    
ob1=A(1)
ob2=A(2)
ob3=A("geeks")
ob4=A("For")

print(ob1 + ob2)
print(ob3 + ob4)