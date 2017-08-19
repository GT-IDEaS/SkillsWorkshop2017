N= 0
M = 0
P = 0

for i in range(1,333+1):
    n=3*i
    N=N+n
print(N)

for i in range(1,199+1):
    m = 5*i
    M = M + m
print(M)

for i in range(1,66+1):
    p = 3*5*i
    P = P + p
print(P)

T = N + M - P
print(T)
