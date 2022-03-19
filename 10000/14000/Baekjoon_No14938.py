import sys
import heapq
input = sys.stdin.readline
N, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]


for _ in range(r):
    x, y, z = map(int, input().split())
    graph[x].append((z, y))
    graph[y].append((z, x))


def dijkstra(start):
    queue = []
    cost = [float('inf')] * (N + 1)
    cost[start] = 0
    heapq.heappush(queue, (cost[start], start))
    while queue:
        weight, node = heapq.heappop(queue)

        if cost[node] < weight:
            continue
        for w, n in graph[node]:
            if w + weight < cost[n]:
                cost[n] = w + weight
                heapq.heappush(queue, (cost[n], n))
    return cost

ans = 0
for i in range(1, N + 1):
    temp = 0
    result = dijkstra(i)
    for j in range(1, N + 1):
        if result[j] <= m:
            temp += item[j]
    ans = max(ans, temp)
print(ans)
