"""
Created on Fri Jul 21 10:17:21 2017
This short program will sum all of the even numbers in the fibonnacci
sequence less than 4 million.
@author: cbalusek3
"""

i1 = 1
i2 = 2
cum = 0
while i2 < 4000000:
    itemp = i2
    i2 += i1
    i1 = itemp
    if i2%2 == 0:
        cum += i2
print(cum) 
