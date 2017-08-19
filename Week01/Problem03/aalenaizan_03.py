number = 600851475143
maximum = number
i = 2
divisor = 1
while i < maximum+1:
	if maximum%i == 0:
		maximum /= i
		continue 
	i += 1
print("Largest prime factor of %i is %i" %(number,i))
