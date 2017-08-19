#What is the largest prime factor of the number 600851475143 ?

import math


def isPrime(num2check):
    i=2

    #need the <= to allow square numbers to be decomposed
    while (i <= math.sqrt(num2check)):
        # for free whatever comes out of this has to be prime, since we search starting from 2.
        # Non prime-factors have to be larger than their prime factors!
        if (num2check % i ==0):
            return i
        else:
            i+=1
            #print(i)
    #if we got here without returning then it's prime
    return 1
#enddef


def main(prod):

    #prod = 13195;
    print(isPrime(25))

    rem = prod;
    isPrimeFlag = 0
    all_prime_factors = []

    #if the return is 1, it's prime, otherwise return the factor you found

    #initially checked from 1 to num. Could stop at sqrt(num2check)?


    # test cases for isPrime
    #print isPrime(7)
    #print isPrime(15)
    #print isPrime(prod)


    while isPrimeFlag==0:
        prime_factor = isPrime(rem)

        if prime_factor==1:
            isPrimeFlag = 1
            print("done: {:1.0f}".format(rem))
            #here the remainder is the largest prime factor
            all_prime_factors.append(int(rem))

        else:
            print("remainder is {:1.0f} * {:1.0f}".format(rem,prime_factor))
            rem = rem/prime_factor
            all_prime_factors.append(prime_factor)

    print(all_prime_factors)
    return all_prime_factors


#appended this to stop this script executing when 05 imports it!
if __name__ == "__main__":
    print("wasn't imported")
    main(600851475143)
    #main(100)
else:
    print("thanks for reusing code!")

