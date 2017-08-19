#!/usr/bin/env python3

"""This script is written by Chuanping Yu, on Jul 24, 2017,
for the Assignment#1 in IDEaS workshop"""

#Problem 5
from fractions import gcd
def lcm(int1, int2):
    """Calculate the least common multiple of two integers, a and b."""
    return int(int1*int2/gcd(int1, int2))
from functools import reduce
print(reduce(lcm, range(1, 20+1)))
