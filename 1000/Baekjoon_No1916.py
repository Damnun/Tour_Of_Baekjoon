import heapq
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
start, end = map(int, input().split())
cost = [float('inf')] * (n + 1)
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
print(cost[end])
