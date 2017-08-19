#!/usr/local/bin/python3.6

def palindrome(n):
	a = 10
	num = []
	while(n//a > 0):
		num.append(n%a)
		n = n//a
	num.append(n)
	flag = 0
	p = len(num)
	for i in range(p//2):
		if(num[i] == num[p-i-1]):
			continue
		else:
			flag = 1
			break
	if(flag == 0):
		return True
	else:
		return False

lar_pal = 0
flag = 0
def calcpal(start):
	for i in range(start,start+100):
		for j in range(start,start+100):
			n = i*j
			if palindrome(n):
				lar_pal = n
	return lar_pal

for i in range(1,10):
	pal = calcpal((10-i)*100)
	if (pal>0):
		break

print("Largest Palindrome =",pal)			







