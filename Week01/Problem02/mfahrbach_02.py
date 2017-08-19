fib = [1, 2]
while fib[-1] < 4000000:
    fib.append(fib[-1] + fib[-2])
print(sum(n for n in fib if n % 2 == 0))
