#!/usr/bin/env python3

"""This script is written by Chuanping Yu, on Jul 24, 2017,
for the Assignment#1 in IDEaS workshop"""

#Problem 1
A = list(range(3, 1000, 3))
B = list(range(5, 1000, 5))
C = list(set(A)|set(B))
print(sum(C))
