import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        a[i][j] += tmp[j]

for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()
