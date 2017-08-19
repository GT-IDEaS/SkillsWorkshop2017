"""
Created on Fri Jul 21 11:20:45 2017
The goal of this program is to find the largest palindromic number formed by two three digit numbers
It can be modified slightly to produce a list of palindromes and the integers that generate them.
@author: cbalusek3
"""

nList = range(999,900,-1)
test = 0
i = 0
for n1 in nList:
    for n2 in nList:
        prod = n1*n2
        if str(prod) == str(prod)[::-1]:
            print(prod, n1 , n2)
            i = 1
            break
    if i == 1:
        break
