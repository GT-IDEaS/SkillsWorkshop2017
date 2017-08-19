large = max(a*b for a in range(101,1000) for b in range(101,1000) if str(a*b) == str(a*b)[::-1])
print(large)
