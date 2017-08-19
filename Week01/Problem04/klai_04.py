def isPalindrome(n):
  l = [int(i) for i in str(n)]
  for i in range(len(l)):
    if (l[i] != l[-1-i]):
      return False

  return True

r = range(100,1000)

z = [x*y for x in r for y in r if isPalindrome(x*y)]

print max(z)
