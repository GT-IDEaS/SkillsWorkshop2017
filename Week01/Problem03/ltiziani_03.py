# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:53:38 2017

@author: Lucas
"""






def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1

n = 600851475143
factor = []

def findFactor(n,factor):
    for i in range(2,n):
        mod = n % i
        if mod == 0:
            factor.append(i)
            n = n//i
            findFactor(n,factor)
            return            
    factor.append(n)
    
findFactor(n, factor)

        