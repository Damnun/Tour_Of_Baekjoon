n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = []
count = 0

for _ in range(m):
    start, end = map(int, input().split())
    if graph[start].count(end) == 0:
        graph[start].append(end)
    if graph[end].count(start) == 0:
        graph[end].append(start)


def dfs(data, root):
    queue = [root]
    global count
    count += 1
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            for i in sorted(data[n]):
                queue.append(i)
    return visited


dfs(graph, 1)
print(count)
