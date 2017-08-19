import math

def findpFactor(n):
  if n == 1:
    return -1
  for i in range(2,(int)(math.floor(math.sqrt(n)))+1):
    if n%i == 0:
      return i

  return -1


def findAllFactors(n):
  facts = []
  x = 0
  while True: 
    x = findpFactor(n)
    print n, x
    if x == -1:
      facts.append(n)
      break
    facts.append(x)
    n = n/x

  return facts

print findAllFactors(600851475143)


