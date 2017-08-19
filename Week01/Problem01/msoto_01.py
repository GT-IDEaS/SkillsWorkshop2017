#!/usr/bin/env python

#Find the sum of all the multiples of 3 or 5 below 1000

add=0
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0): 
    	add += i
    else:
    	continue
    
print(add)

