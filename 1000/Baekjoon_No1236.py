import sys
input = sys.stdin.readline
n, m = map(int,input().split())
a, b = 0, 0
data = []

for _ in range(n):
    data.append(input())

for i in range(n):
    if "X" not in data[i]:
        a += 1

for j in range(m):
    if "X" not in [data[i][j] for i in range(n)]:
        b += 1

print(max(a ,b))
