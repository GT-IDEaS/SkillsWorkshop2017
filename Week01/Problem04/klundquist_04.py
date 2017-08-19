
#Largest Palindrome Product
i = 0
b = True
while i <= 100 and b:
    j = 0
    while j<= 100 and b: 
        num1 = 999 - i
        num2 = 999 - j
        res = num1 * num2
        res_str = str(res)
        if res_str[0] == res_str[5] and res_str[1] == res_str[4] and res_str[2] == res_str[3]:
            print(str(num1) + " * " + str(num2) + " = " + res_str)
            b = False
            break
        j = j + 1
    i = i + 1
