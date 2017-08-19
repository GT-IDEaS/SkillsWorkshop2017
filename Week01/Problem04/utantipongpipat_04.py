import math

def parTest(number):
    strIn = str(number);
    for i in range (math.floor(len(strIn)/2)):
        if (strIn[i] != strIn[len(strIn)-i-1]):
            return False;
    return True;
#parTest(356654) for testing

n=100;
maxPar = -1;
for a in range(n):
    for b in range(n):
        #brute force all product of 2 numbers starting from 999 * 999 can go lower
        number = (999 - a)*(999-b);
        if number > maxPar and parTest(number):
            maxPar = number;
print(maxPar)
            