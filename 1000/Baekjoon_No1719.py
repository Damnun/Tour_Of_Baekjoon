import heapq
N, m = map(int, input().split())
graph = [[] for _ in range(N + 2)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

result = []

for start in range(1, N + 1):
    path = [-1 for _ in range(N + 2)]
    cost = [float('inf')] * (N + 2)
    cost[start] = 0

    queue = []
    heapq.heappush(queue, (cost[start], start))
    while queue:
        weight, node = heapq.heappop(queue)

        if cost[node] < weight:
            continue
        for w, n in graph[node]:
            if w + weight < cost[n]:
                cost[n] = w + weight
                heapq.heappush(queue, (cost[n], n))
                path[n] = node
    result.append(path)

for i in range(1, N + 1):
    for j in range(N):
        if i == j + 1:
            print('-', end=' ')
        else:
            print(result[j][i], end=' ')
    print()
