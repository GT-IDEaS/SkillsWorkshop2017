def lpf(x):
    i = 2
    while i * i <= x:
        if (x % i != 0):
            i += 1
        else:
            x //= i
    return x

n = 600851475143	 
print(lpf(n))
# 6857
