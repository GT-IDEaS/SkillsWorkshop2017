#!/usr/bin/env python3

"""This script is written by Chuanping Yu, on Jul 24, 2017,
for the Assignment#1 in IDEaS workshop"""

#Problem 4
S = 0
A = 0
B = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        num = a*b
        if str(num) == str(num)[::-1] and S < num:
            S = num
            A = a
            B = b
print(S, "=", A, "*", B)
