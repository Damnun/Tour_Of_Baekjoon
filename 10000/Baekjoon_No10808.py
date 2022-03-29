import sys
from collections import Counter
c = Counter(list(map(str,sys.stdin.readline().strip())))
res = []

for i in range(26):
    res.append(c[chr(97 + i)])
print(*res)
