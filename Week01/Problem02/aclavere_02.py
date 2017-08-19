#!/usr/bin/env python
sol = 0
x, y = 1, 2
while y < 4000000:
    x, y = y, x + y
    if x%2==0:
        sol += x
print (sol)
