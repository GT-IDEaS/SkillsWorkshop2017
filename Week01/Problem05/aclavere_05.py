#!/usr/bin/env python
n=20
count=0
restart=True

while restart:
    restart=False
    for x in range (1,21):
        if n%x==0:
            count+=1
            if count==20:
                print(n)
                break
        else:
            n+=1
            count=0
            restart=True
            break
