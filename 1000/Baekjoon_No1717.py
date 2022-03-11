import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
p = [i for i in range(n + 1)]


def union(a, b):
    a, b = find(a), find(b)

    if a > b:
        p[a] = b
    else:
        p[b] = a


def find(u):
    if p[u] == u:
        return u
    p[u] = find(p[u])
    return p[u]


for _ in range(m):
    f, x, y = map(int, input().split())

    if f:
        if find(x) == find(y):
            print('YES')
        else:
            print('NO')
    else:
        union(x, y)
