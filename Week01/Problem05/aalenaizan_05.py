def primeFactors(x):
	factors = []
	i = 2
	while i < x+1:
		if x%i == 0:
			factors.append(i)
			x /= i
		else:
			i = i + 1
	return factors

def LCM(factors):
	prime_list = []
	for i in factors:
		prime_list.append(primeFactors(i))
	LCM = 1
	for i in prime_list:
		for j in i:
			LCM *= j
			for i in prime_list:
				if j in i:
					i.remove(j)
	return LCM

print LCM(range(2,21))
