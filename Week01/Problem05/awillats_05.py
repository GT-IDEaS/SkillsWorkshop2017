#2520 is the smallest number that can be divided
# by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number
# that is evenly divisible by all of the numbers from 1 to 20?



#reuse my code from problem 3 for checking for primes

#using counters instead of multiset API


import sys
sys.path.append('../Problem03')
#from awillats_03 import isPrime
import awillats_03


from collections import Counter
#import multiset


#may want to functionalize the decomposition in problem 3 also...

max_factor = 20

prod =1


all_prime_factors = Counter()


for i in range(1,max_factor+1):
   individual_facts = awillats_03.main(i)

   #uses the union operator for counters to update the multiplicity of prime factors
   all_prime_factors = (all_prime_factors | Counter(individual_facts))

print(all_prime_factors)


for k,v in all_prime_factors.items():
    prod = prod*(k**v)

print(prod)