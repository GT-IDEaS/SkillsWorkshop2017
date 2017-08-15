#!/usr/bin/env python

#By considering the terms in the Fibonacci sequence whose values do not 
#exceed four million, find the sum of the even-valued terms.

sum = 0
a=0
i=1
#c=
while i < 4000000:
	i=a+i
	a=i-a
	if (i%2==0):
		sum+=i
print(sum)

