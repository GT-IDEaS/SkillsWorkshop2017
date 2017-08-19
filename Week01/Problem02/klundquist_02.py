
fib = []
fib.append(1)
#print(0,1,0)
fib.append(2)
#print(1,2,2)

i = 2

total = 2
while 1:
    fib.append(fib[i-1] + fib[i-2])
    if fib[i] > 4000000:
        print(total)
        break
    if fib[i]%2 == 0:
        total = total + fib[i]
    #print(i,fib[i],total)
    i = i + 1
