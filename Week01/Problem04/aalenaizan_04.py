i = 999
lower = 0
largestPalindrome = 0

while i > 99:
	j = 999
	j -= lower
	while j > 99:
		x = str(i*j)
		if x == x[::-1] and i*j > largestPalindrome:
			largestPalindrome = i*j
			factor1 = i
			factor2 = j
		j -= 1
	lower += 1
	i -= 1

print largestPalindrome, factor1, factor2
