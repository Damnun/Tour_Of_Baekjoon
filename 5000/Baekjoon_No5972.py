import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
cost = [float('inf')] * (n + 1)
start = 1

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

cost[start] = 0
queue = []
heapq.heappush(queue, (0, start))

while queue:
    weight, node = heapq.heappop(queue)

    if cost[node] < weight:
        continue
    for w, n in graph[node]:
        if w + weight < cost[n]:
            cost[n] = w + weight
            heapq.heappush(queue, (cost[n], n))
print(cost[-1])
