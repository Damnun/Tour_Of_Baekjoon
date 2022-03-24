import sys
input = sys.stdin.readline


def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]


def union(p, a, b):
    a = find(p, a)
    b = find(p, b)

    if a < b:
        p[b] = a
    else:
        p[a] = b


n, m, k = map(int, input().split())
f = list(map(int, input().split()))
p = [i for i in range(n + 1)]

for _ in range(m):
    v, w = map(int, input().split())
    union(p, v, w)

ans = 0
visited = set()
for i in range(1, n + 1):
    if i not in visited:
        tmp = [i]
        cost = f[i - 1]
        for j in range(1, n + 1):
            if i != j:
                if find(p, i) == find(p, j):
                    tmp.append(j)
                    cost = min(cost, f[j - 1])
        visited.update(tmp)
        ans += cost

if k >= ans:
    print(ans)
else:
    print("Oh no")
