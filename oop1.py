# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:24:39 2019

@author: DELL
"""

class Employee:
    'common base class for all emplyes'
    empCount =0
    def Employee(self):
        print("Total Employee %d"%Employee.empCount)
        
    def  __init__(self,name,salary):
        print("Constructor created")
        self.name =name
        self.salary=salary
        Employee.empCount+=1
        
    def displaycount(self):
        print("Total Employee %d "%Employee.empCount)
        
    def displayemployee(self):
        print("name :",self.name,",salary :",self.salary)
"This would create first object employee class"
emp1=Employee("zara",2000)
emp1.displayemployee()
"This would create second object employee class"
emp2=Employee("yogi",4000)