
num = 1
incr = 1
j = 1
while j <= 20: 
    found = False
    k = 1
    while found == False:
        found = True
        num = incr * k
        i = 1
        while  i <= j:
            if num % i != 0:
                found = False
                break
            i = i + 1
        k = k + 1
    print(str(j) + " " + str(num))
    incr = num
    j = j + 1
