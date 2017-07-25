# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:24:29 2017

@author: Lucas
"""

s = 0 # sum of multiples

for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
        s = s + n
        
print(s)
    
