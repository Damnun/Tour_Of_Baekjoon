import sys
input = sys.stdin.readline


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        p[y] = x
    else:
        p[x] = y

n, m = map(int, input().split())
p = [0] + [i for i in range(1, n + 1)]
ans = 0
for i in range(1, m + 1):
    a, b = map(int, input().split())
    if find(a) == find(b):
        ans = i
        break
    union(a, b)
print(ans)
