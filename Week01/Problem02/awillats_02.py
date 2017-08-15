#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

import math
#max_num = int(1000)
max_num = int(4e6)

old_fib = 0
fib = 1
new_fib = 0

sum_fib = 0

#while fib < max_num:

#needed to check before sum
#then fibs were wrong

#printed to check fibs, figured out

while fib <= max_num:

    #print(fib,"+",old_fib,"=",fib+old_fib)

    #C-style formatting
    print("C: %i + %i = %i" % (fib,old_fib,fib+old_fib),end="")

    #new python formatting
    print("  Py: {:d} + {:d} = {:d}".format(fib,old_fib,fib+old_fib))


    if (fib % 2 ==0):
        sum_fib += fib
        #print sum_fib

    new_fib = fib+old_fib
    old_fib = fib
    fib = new_fib

print(sum_fib)
