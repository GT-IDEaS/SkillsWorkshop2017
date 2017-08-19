n = 600851475143
m = int(n**0.5)
p = 1
for i in range(2, m + 1):
    while n % i == 0:
        n /= i
        p = i
print(max(p, n))
