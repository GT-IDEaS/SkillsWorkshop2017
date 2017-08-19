from __future__ import print_function

def max():
    d = range(20, 10, -1) # only check multiple of 11 through 20 
    n = 20

    while True:
        for x in d:
            if n % x != 0:
                break
        else: # no break happened, all multiples
            return n
        n += 20 # multiple of 20 should come in increments of 20

print(max())
