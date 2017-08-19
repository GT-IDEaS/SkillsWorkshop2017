#!/usr/bin/env python
n = 600851475143
i = 2

while i< n:
    if n%i == 0:
        n = n / i
    else:
        i+=1

print (n)
