import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
result = set()

for i in range(1, n + 1):
    for cur in combinations(data, i):
        result.add(sum(cur))

result = sorted(list(result))
idx = 1
for i in result:
    if i != idx:
        break
    idx += 1
print(idx)
