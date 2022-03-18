import sys
input = sys.stdin.readline
V, S = map(int, input().split())

graph = []
for _ in range(S):
    a, b, w = map(int ,input().split())
    graph.append((w, a, b))
graph.sort()
p = list(range(V + 1))


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        p[b] = a
    else:
        p[a] = b


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


ans = 0
for w, s, e in graph:
    if find(s) != find(e):
        union(s, e)
        ans += w
print(ans)
