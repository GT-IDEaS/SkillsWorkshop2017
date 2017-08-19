term1 = 1
term2 = 2
summ = 0

while term2 < 4000001:
	if term2%2 == 0:
		summ =+ term2
	temp = term2
	term2 = term1 + term2
	term1 = temp

print(summ)
