from __future__ import print_function

# using generators here to create a "stream" of fibonacci numbers that we can
# test for evenness

def fib(limit=4000000):
    F = [1, 2]
    i = 2 

    for x in F:
        yield x

    while F[-1] < limit:
        F.append(F[i - 1] + F[i - 2])
        yield F[-1]
        i += 1

print(sum(x for x in fib() if x % 2 == 0))
