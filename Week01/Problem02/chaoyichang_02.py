i,j=1,2
sum=0
while j <4000000:
	i,j=j,i+j
	if i%2==0:
		sum=sum+i
print sum