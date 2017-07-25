# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 10:07:39 2017

@author: Lucas
"""

n = 2520


while True:
    d = True
    for i in range(1,21):
        mod = n % i
        d = d and mod == 0
    if d == True:
        print(n)
        break
        
    n = n + 2520