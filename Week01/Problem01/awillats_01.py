
# sum multiple of 3,5 less than 1000

import math

sum_var = 0

num_max = 1000

for i in range(num_max):
    if (i % 3 == 0):
        sum_var +=i
    elif (i % 5 == 0):
        sum_var +=i


# for i in range(int(math.floor(1000/3))):
#     sum_var += i*3
#
# for i in range(int(math.floor(1000/5))):
#     sum_var += i*5

print(sum_var)
