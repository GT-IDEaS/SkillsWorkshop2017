import math;

def lcm(a,b):
    return a//math.gcd(a,b)*b;

answer = 1;
for i in range(2,21):
    answer = lcm(answer,i); #lcm of all 1,2,3,...,20

print(answer)
    