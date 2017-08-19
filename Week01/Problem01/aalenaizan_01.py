i = 0
summ = 0

while i < 1000:
	if (i%3 == 0) or (i%5 == 0):
		summ += i
	i += 1

print(summ)
