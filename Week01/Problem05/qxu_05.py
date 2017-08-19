# define gcd function
def gcd(x, y):
   #Use Euclidian algorithm to find Greatest Common Divisor
	if y > x:
		x, y = y, x
	while(y != 0):
		x, y = y, x % y
	return x

def lcm(x,y):
	return x * y // gcd(x,y) 
	
number = 1 # Initialize the number to be the first number
for ii in range(2,21):
	number = lcm(number,ii)

print('LCM of 1 to 20 is:',number)
# LCM of 1 to 20 is: 232792560