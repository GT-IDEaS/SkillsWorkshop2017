#!/usr/bin/env python
sol=0
for a in range(999,99,-1):
    for b in range (999,99,-1):   
        pal=a*b
        if (str(pal)==str(pal)[::-1]):
            if pal>sol:
                sol=pal
print(sol)
