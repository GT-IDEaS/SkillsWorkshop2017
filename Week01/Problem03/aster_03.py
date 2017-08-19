# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:33:52 2017

@author: Aster
"""

def ProjectEuler_problem3(N):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    def find_two_factors(n):
        flag = 0
        k = 2
        factor1,factor2 = 0,0
        while flag == 0 and k <= n/2:
            if n % k == 0:
                factor1,factor2 = k,int(n/k)
                flag = 1
            else:
                k += 1
        return factor1,factor2
        
    to_be_factorized = [N]
    factors = []
    count = 1
    while len(to_be_factorized) and count < 4000:
        count += 1
        f0 = to_be_factorized[0]
        factor1,factor2 = find_two_factors(f0)
        if not factor1:
            factors.append(f0)
            del to_be_factorized[0]
        else:
            del to_be_factorized[0]
            to_be_factorized.append(factor1)
            to_be_factorized.append(factor2)
#    print('factors',factors)
    print('ans_P3 = ',max(factors))
        
ProjectEuler_problem3(600851475143)