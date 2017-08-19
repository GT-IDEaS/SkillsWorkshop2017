#!/usr/local/bin/python3.6
a = 600851475143
prime = [];
prime.append(2)
def nextprime():
	n = prime[-1]
	m = n
	while(m == prime[-1]):
		flag = 1
		n = n+1
		for i in prime:
			if (n%i == 0):
				flag = 0
				break
		if (flag == 1):
			m = n
	prime.append(m)
	return prime[-1]

b = a
while(b > 1):
	if(b%prime[-1] == 0):
		b = b/prime[-1]
	else:
		nextprime()
print("The largest prime factor of",a,"=",prime[-1])



       	


