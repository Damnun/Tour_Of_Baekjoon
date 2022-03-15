import heapq
m, e = map(int, input().split())
graph = [[] for _ in range(m + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    # 양방향 그래프
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, input().split())


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
            if w + weight < cost[n]:
                cost[n] = w + weight
                heapq.heappush(queue, (cost[n], n))
    return cost[end]


answer = djikstra(1, v1) + djikstra(v1, v2) + djikstra(v2, m)
answer2 = djikstra(1, v2) + djikstra(v2, v1) + djikstra(v1, m)
answer = min(answer, answer2)
if answer == float('inf'):
    print(-1)
else:
    print(answer)
