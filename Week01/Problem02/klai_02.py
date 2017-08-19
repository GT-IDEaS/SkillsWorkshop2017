upper = 4e6


def f(n):
  fib = []
  for i in range(n):
    if i == 0:
      fib.append(1)
    elif i == 1:
      fib.append(2)
    else:
      fib.append(fib[i-1] + fib[i-2])

  return fib


x = f(50)

l = [x[i] for i in range(50) if x[i]%2 == 0 and x[i] <= upper]
print sum(l)
