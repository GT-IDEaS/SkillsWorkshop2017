# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:31:19 2017

@author: Aster
"""

import math

def ProjectEuler_problem1(n1,n2,N):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    N  = N-1 # multiple strictly less than N
    K1 = math.floor(N/n1)
    K2 = math.floor(N/n2)
    L1 = [ n1 * k for k in range(1,K1+1)]
    L2 = [ n2 * k for k in range(1,K2+1) if n2*k not in L1]
    my_sum = 0
    for n in L1 + L2:
        my_sum += n
    print('ans_P1 = ',my_sum)

ProjectEuler_problem1(3,5,1000)