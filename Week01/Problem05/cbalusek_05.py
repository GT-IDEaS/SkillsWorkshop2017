"""
Created on Fri Jul 21 10:43:01 2017
It isn't pretty coding (and definitely ins't optimized) but it gets the job done
@author: cbalusek3
"""

def get_primes(n):
    nlist = set(range(n,1,-1)) 
    primes = []
    for i in nlist:
        testList = []
        for p in primes:
            if i%p != 0:
                testList.append(i)
        if len(testList) >= len(primes):
            primes.append(i)
    return primes

def get_pFactor(n):
    plist = get_primes(20)
    factorList = []
    for p in plist:
        m = n
        while m >= p:
            if m%p == 0:
                factorList.append(p)
            m = m/p
    return factorList

fullFactorList = []       
for j in set(range(20,1,-1)):
    newj = get_pFactor(j)
    for i in newj:
        while fullFactorList.count(i) < newj.count(i):
            fullFactorList.append(i)
prod = 1
for i in fullFactorList:
    prod *= i
print(prod)
