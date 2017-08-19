import numpy as np

def isPrime(val):
    factorList = [val]
    if val <= 20000:
        ints = set(range(2,val-1,1))
    if val > 20000:
        ints = set(range(3,int((val-1)/2),2))
    for i in ints:
        if val%i == 0 or val%2 == 0:
            factorList.append(i)
            return 0
            break
    if len(factorList) == 1:
        return 1

def get_pFactor(n):
    factorList = []
    if n <= 20000:
        ints = set(range(2,n,1))
    elif n > 20000 and n < 2000000:
        ints = set(range(3,int(n/2),2))
    else:
        ints = set(range(3,2000000,1))
    for p in ints:
        if n%p == 0:
            if isPrime(p) == 1:
                factorList.append(p)
    return np.amax(factorList)
        
print(get_pFactor(600851475143))
