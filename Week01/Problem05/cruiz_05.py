#!/usr/bin/env python

num = 20
count = 0
should_restart = True


while should_restart:
    should_restart = False
    for i in range(1,21):
        if num%i == 0:
            count += 1
            if count == 20:
                print(num)
                break
        else:
            num += 1
            count = 0
            should_restart = True
            break

