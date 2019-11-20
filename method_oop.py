# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:43:46 2019

@author: DELL
"""
class Employee:
    'common base class for all emplyes'
    empCount =0
    
    def  __init__(self,name,salary):
        self.name =name
        self.salary=salary
        Employee.empCount+=1
        
    def displaycount(self):
        print("Total Employee %d "%Employee.empCount)
        
    def displayemployee(self):
        print("name :",self.name,",salary :",self.salary)

emp1=Employee("meng",1000000)
emp=Employee("yogi",2000000)
emp.displaycount()
emp.displayemployee()
emp1.displayemployee()
Employee.empCount