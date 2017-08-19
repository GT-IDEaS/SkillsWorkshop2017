#!/usr/bin/env python

sum = 0
i = 1
j = 1
while i < 4000000:
    a = i
    i += j
    j = a
    if (i%2==0 and i<4000000):
        sum += i
print(sum)
