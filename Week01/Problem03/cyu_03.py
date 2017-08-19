#!/usr/bin/env python3

"""This script is written by Chuanping Yu, on Jul 24, 2017,
for the Assignment#1 in IDEaS workshop"""

#Problem 3
I = 3
N = 600851475143
F = []
while I*I <= N:
    if N%I == 0:
        N = int(N/I)
        F.append(I)
    else:
        I = I + 1
if N > 1:
    F.append(N)
print(F)
