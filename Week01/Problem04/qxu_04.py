palindromic = 0
for ii in range(100,1000):
	for jj in range(ii,1000):
		prod = ii * jj
		prodstr = str(prod)
		flag = 1
		for d in range(len(prodstr)//2):
			if prodstr[d] != prodstr[len(prodstr)-d-1]:
				flag = 0
				break
		if flag == 1 and prod > palindromic:
			palindromic = prod
			x = ii
			y = jj
print(x,'x',y,'=',palindromic)
# 913 x 993 = 906609