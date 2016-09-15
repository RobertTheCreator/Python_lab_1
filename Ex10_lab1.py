    s = str(input())
k = s.replace('h', 'H', s.count('h')-1)
k = k.replace('H', 'h', 1)
print(k)