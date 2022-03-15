import heapq
n, m, x = map(int, input().split())
graph = [[] for _ in range(m + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))


def djikstra(start, end):
    cost = [float('inf')] * (m + 1)
    cost[start] = 0
    queue = []
    heapq.heappush(queue, (cost[start], start))

    while queue:
        weight, node = heapq.heappop(queue)

        if cost[node] < weight:
            continue
        for w, n in graph[node]:
            if weight + w < cost[n]:
                cost[n] = weight + w
                heapq.heappush(queue, (cost[n], n))
    return cost[end]

answer = [0] * (n + 1)
for i in range(1, n + 1):
    answer[i] = djikstra(i, x) + djikstra(x, i)
print(max(answer))
