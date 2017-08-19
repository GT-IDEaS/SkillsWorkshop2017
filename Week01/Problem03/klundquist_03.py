#What is the largest prime factor of number
import math
#number = 13195
number = 600851475143

def isPrime( value ):
    ip_bool = True
    j = 2
    while j < value:
        if value % j == 0:
            ip_bool = False
            break
        j = j + 1
    return ip_bool

i = 3
i_max = math.ceil(math.sqrt(number))
lpf = 0 # largest prime factor
while i < i_max:
    if number % i == 0:
        if isPrime(i):
            lpf = i
    i = i + 2
print(lpf)

