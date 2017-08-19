#!/usr/bin/env python

number = 600851475143
i=2
current = 0
while i < number:
    if (number%i == 0):
        number = number/i
    else:
        i+=1
print(int(number))

