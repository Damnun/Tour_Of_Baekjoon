import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    cost = [float('inf')] * (n + 1)

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))

    cost[c] = 0
    queue = []
    heapq.heappush(queue, (0, c))
    while queue:
        weight, node = heapq.heappop(queue)

        if cost[node] < weight:
            continue
        for w, n in graph[node]:
            if w + weight < cost[n]:
                cost[n] = w + weight
                heapq.heappush(queue, (cost[n], n))

    max = 0
    count = 0
    for i in cost:
        if i != float('inf'):
            if i > max:
                max = i
            count += 1
    print(count, max)
