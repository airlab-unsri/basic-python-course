# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:22:28 2019

@author: DELL
"""
class Computer:
    def  __init__(self):
        self._maxprice=900
        
    def sell(self):
      print("Selling price: {}".format(self._maxprice))
    
    def setMaxPrice(self,price):
        self._maxprice=price
        
c= Computer()
c.sell()

# Change The Price 
c._maxprice=1000
c.sell()

#Using Setter Function
c.setMaxPrice(1500)
c.sell()