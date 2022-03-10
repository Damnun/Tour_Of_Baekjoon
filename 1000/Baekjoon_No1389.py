from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, start):
    p = [0] * (n + 1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if i not in visited:
                p[i] = p[cur] + 1
                visited.append(i)
                queue.append(i)
    return sum(p)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = []
for i in range(1, n + 1):
    result.append(bfs(graph, i))
print(result.index(min(result)) + 1)
