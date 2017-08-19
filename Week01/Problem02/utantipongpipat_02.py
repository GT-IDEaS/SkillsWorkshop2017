ans = 0;
num1 = 1;
num2 = 2;
while (num2 < 4000000):
    if (num2%2 == 0):
        ans = ans + num2;
    num3 = num1 + num2;
    num1 = num2;
    num2 = num3;
print(ans)