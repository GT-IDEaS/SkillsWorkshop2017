#!/usr/bin/env python

##What is the largest prime factor of the number 600851475143?

i=2
number=600851475143
while i < number:
	while number%i == 0:
		number = number/i
	i+=1
print(number) 
	
