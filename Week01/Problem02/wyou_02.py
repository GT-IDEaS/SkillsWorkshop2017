a = 1
b = 1
c = a + b
sum = 0

limit = 4000000

while (c < limit):
    sum += c
    a = b + c
    b = c + a
    c = a + b
print(sum)
