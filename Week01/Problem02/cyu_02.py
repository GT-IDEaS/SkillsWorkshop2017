#!/usr/bin/env python3

"""This script is written by Chuanping Yu, on Jul 24, 2017,
for the Assignment#1 in IDEaS workshop"""

#Problem 2
FIB = []
F = 1
S = 0
FIB.append(F)
FIB.append(F)
while F <= 4000000:
    F = FIB[-1] + FIB[-2]
    FIB.append(F)
    if F%2 == 0 and F <= 4000000:
        S = S + F
print(S)
