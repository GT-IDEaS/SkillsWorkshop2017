#import euler3 as el
from operator import mul

primes = [2,2,2,2,3,3,5,7,11,13,17,19]
print reduce(mul, primes, 1)


