sum = 0
Fib = 0
Fib_prev1 = 1
Fib_prev2 = 0
while Fib <= 4000000:
	Fib = Fib_prev1 + Fib_prev2
	if Fib % 2 == 0:
		sum += Fib
	Fib_prev2 = Fib_prev1
	Fib_prev1 = Fib
print(sum)
# 4613732
