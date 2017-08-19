# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:34:52 2017

@author: Aster
"""

def ProjectEuler_problem4(N):        
    """
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    palindromics = []
    for n1 in range(10**(N-1),10**N):    
        for n2 in range(10**(N-1),10**N):
            prod = n1 * n2
            prod_str = str(prod)
            ndigits = len(prod_str)
            if prod_str[0] == prod_str[ndigits-1]:
                flag = 0
                i = 1
                while i <= ndigits/2 and flag == 0:
                    if prod_str[i] == prod_str[-(i+1)]:
                        i += 1
                    else:
                        flag = 1
                if flag == 0:
                    palindromics.append(prod)
                    
#    print(palindromics)
    print('ans_P4 = ',max(palindromics))
    
ProjectEuler_problem4(3)