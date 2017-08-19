# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:38:07 2017

@author: Aster
"""
import math
def ProjectEuler_problem5(N):   
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    flag = 0
    n = N
    while flag == 0:
        flag1 = 0
        k = math.floor(N/2) # numbers smaller than N/2 don't need to be considered
        NN = list(range(math.floor(N/2),N))
        while k  < N and flag1 == 0:
            if k in NN:
                if n % k != 0:
                    flag1 = 1 
            k += 1
        if flag1 == 0:
            flag = 1
        else:
            n += 1
    print('ans_N10 = ',n)
    
ProjectEuler_problem5(10)
"""
The code above will take to long to run if we use N = 20.
I would have to make it more efficient.
But the answer for this problem is the following:
"""
print('ans_P5 =', 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)
"""
Here is how I obtained it:
1) Find the prime factorization of all integer from 1 to 20 and 
multiply then all:
    2 * 3 * 2^2 * 5 * (2*3) * 7 * 2^3 * ... * 19 * (2^2*5)
This number is too large because there are factors that we don't need.

2) For each prime in the factorization pick the factor with largest power:
    2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19
Any other factor is redundant.
Thus this is the answer!

"""