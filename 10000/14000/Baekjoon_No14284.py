import heapq
N, m = map(int, input().split())
graph = [[] for _ in range(N + 1)]
cost = [float('inf')] * (N + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

s, t = map(int, input().split())
queue = []
cost[s] = 0
heapq.heappush(queue, (cost[s], s))

while queue:
    weight, node = heapq.heappop(queue)
    if cost[node] < weight:
        continue
    for w, n in graph[node]:
        if w + weight < cost[n]:
            cost[n] = w + weight
            heapq.heappush(queue, (cost[n], n))

print(cost[t])
