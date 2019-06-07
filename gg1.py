import sys, string, math, itertools
n1 = input()
n1 = int(n1)
L = []
for i in range(0,n1) :
    s = input()
    L.append(s)
common_prefix = []
for i in zip(*L):
    if i.count(i[0]) == len(i):
        common_prefix.append(i[0])
    else:
        break
ans = ''.join(common_prefix)
print(ans)
