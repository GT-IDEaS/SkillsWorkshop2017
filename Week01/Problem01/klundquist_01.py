
limit = 1000

num = 3
total = 0
while num < limit:
    total = total + num
    num = num + 3

num = 5
while num < limit:
    if num%3 != 0:
        total = total + num
    num = num + 5

print(total)
