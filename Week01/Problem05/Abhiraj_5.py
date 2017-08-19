#!/usr/local/bin/python3.6

prime = [19,17,13,11,7,5,3,2]# primes below 20
n = []
for i in range(1,21):
	n.append(i)
lcm = 1
def checkprime(prime):
	size = len(n)
	flag = 0
	count = 0
	while(count < size):
		if(n[count]%prime == 0):
			n[count] = n[count]//prime
			if (n[count] == 1):
				n.pop(count)
				count -=1
				size = len(n)
			flag = 1
		count+=1
	return flag

for i in prime:	
	while(checkprime(i) == 1):
		lcm*=i
print("LCM of numbers from 1 to 20 = ",lcm)


