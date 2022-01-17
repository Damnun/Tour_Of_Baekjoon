n, m = map(int, input().split())
edges = [[] for _ in range(n)]
visited = [False] * n
result = False

for i in range(m):
    start, end = map(int, input().split())
    edges[start].append(end)
    edges[end].append(start)


def solve(d, x):
    global result
    if d == 4:
        result = True
        return

    for i in edges[x]:
        if not visited[i]:
            visited[i] = True
            solve(d + 1, i)
            visited[i] = False


for i in range(n):
    visited[i] = True
    solve(0, i)
    visited[i] = False
    if result:
        break

if result:
    print(1)
else:
    print(0)
