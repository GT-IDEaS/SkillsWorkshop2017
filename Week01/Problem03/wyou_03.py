n = 600851475143
factor = 2 


primes= []
while n>1:
    if n % factor == 0:
        primes.append(factor)
        n = int(n/factor)
    else: 
        factor += 1

print(primes)
