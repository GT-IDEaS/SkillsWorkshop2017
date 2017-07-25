# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
pals = [] # palindrome

for i in range(100,1000):
    for j in range(100,1000):
        p = 1
        n = i*j
        ns = str(n)
        lns = len(ns)
        
        for k in range(0,lns//2):
            if ns[k] != ns[-k-1]:
                p = 0
        if p == 1:
            pals.append(n)
            
print(max(pals))
