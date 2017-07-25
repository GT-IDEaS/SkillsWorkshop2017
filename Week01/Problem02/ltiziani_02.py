# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:36:31 2017

@author: Lucas
"""

s = 2
n = [1,2]
m = 3

while m <= 4000000:
    n.append(m)

    if n[-1] % 2 == 0: # if even number
        s = s + n[-1]
    
    m = n[-1] + n[-2]
    
print(s)