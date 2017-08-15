import math

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.






def checkIfPal(num):
    #in more robust program would check if the number is an integer here
    str1 = str(int(num))
    #reverse the string through indexing
    str2 = str1[::-1]

    #using ternary operator for condensed code
    return True if (str1==str2) else False

#initially tried to decrement down the range 1000->100 in two nested loops,
# but this meant I didn't find the biggest palindrome.

#now just blindly check all products to see if they're bigger

#put this code in a loop so I could return when the loop was complete
def mainCheckLoop():
    bestPal = 0
    for x in range(1000,100,-1):
        #only have to go up to the size of x for the second number
        for y in range(1000,100,-1):

            prod = x*y
            if checkIfPal(prod) == True:
                if prod > bestPal:
                    print("{:d} = {:d} * {:d}".format(prod, x, y))
                    bestPal = prod

    return bestPal


ans = mainCheckLoop()
print(ans)
