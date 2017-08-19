prev = 1
curr = 2
tmp = 0

limit = 4000000

while (curr < limit):
    if (curr % 2 == 0):
        tmp += curr
    new = prev + curr
    prev = curr
    curr = new

print(tmp)
