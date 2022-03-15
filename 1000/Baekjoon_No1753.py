import sys
import heapq
input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))
    
cost = [float('inf')] * (v + 1)
cost[start] = 0
queue = []
heapq.heappush(queue, (0, start))

while queue:
    weight, node = heapq.heappop(queue)

    if cost[node] < weight:
        continue
    for w, n in graph[node]:
        if weight + w < cost[n]:
            cost[n] = weight + w
            heapq.heappush(queue, (cost[n], n))

for i in cost[1:]:
    print(i if i != float('inf') else "INF")
