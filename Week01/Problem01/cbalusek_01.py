#This project defines a function that takes any two numbers and sums their multiples to some cutoff value

def sum(val1, val2, test):
    i = 1
    j = 1
    cum = 0
    while i*val1 < test:
        cum += i*val1
        i += 1
    while j*val2 < test:
        if j*val2%val1 != 0:
            cum += j*val2
            j += 1
        else:
            j += 1
    return cum

print(sum(3,5,1000))
