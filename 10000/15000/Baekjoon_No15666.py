from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
data = []

for i in combinations_with_replacement(a, m):
    i = sorted(list(i))
    if i not in data:
        data.append(i)

data = [sorted(i) for i in data]
data.sort()

for i in data:
    for j in i:
        print(j, end=" ")
    print()
