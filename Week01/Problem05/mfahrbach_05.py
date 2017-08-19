
from math import gcd
ans = 1
for i in range(2, 21):
    ans = i*ans//gcd(i, ans)
print(ans)