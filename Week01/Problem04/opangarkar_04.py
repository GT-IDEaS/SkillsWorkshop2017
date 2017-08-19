from __future__ import print_function
from itertools import combinations

# simple, extract digits in a list
# check for equality between list and reversed(list)
def ispal(n):
    x = []
    while n > 9:
        x.append(n % 10)
        n = n / 10
    x.append(n)
    return True if x == list(reversed(x)) else False

# brute force the solution, start with largest pairs of numbers
# like (999, 999)
maxprod = 0
for i in combinations(range(999, 0, -1), 2):
    prod = i[0] * i[1]
    if ispal(prod):
        if prod > maxprod:
            maxprod = prod

print(maxprod)
