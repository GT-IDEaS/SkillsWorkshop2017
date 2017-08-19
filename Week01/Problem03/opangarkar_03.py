from __future__ import print_function
from math import sqrt

# little tricky, each call of the function is tracking
# the largest prime we have got till now (c), starting with 2
# we keep dividing the number into pieces and keep track of
# this largest prime until the number itself is its largest
# prime or we fail the condition on line 13 that if current number i
# multiplied by largest prime c till now exceeds the number itself
# that means there are no more greater primes than c

def largest_prime(n, c=2):
    i = c
    while i * c <= n:
        if n % i == 0:
            x = largest_prime(n / i, i)
            break
        i += 1
    else:
        return n
    return x

print(largest_prime(600851475143))

