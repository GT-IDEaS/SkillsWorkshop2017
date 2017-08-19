import math
number = 600851475143;
prime = 2;
biggestPrime = 2;
#will pull out prime factor, from small one first
while (prime < number+1 ):
    while (number%prime == 0):
        number = number/prime;
        biggestPrime = prime; #this prime is a factor
    prime=prime+1; #even if prime is not really a prime, e.g. 4, it's ok because the factor of 4 is already out from original number
print(biggestPrime)