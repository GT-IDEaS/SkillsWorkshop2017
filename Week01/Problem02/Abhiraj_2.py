#!/usr/local/bin/python3.6
a = 1
b = 1
sum = 0
c = a+b
while(c < 4*(10**6)):
	if (c%2 == 0):
		sum +=c
	a = b
	b = c
	c = a+b
print("Sum of even-valued terms in Fibonacci sequence = ",sum)	


