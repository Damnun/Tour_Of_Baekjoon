import heapq
def dijkstra(start):
    cost = [float('inf')] * (N + 1)
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

    return cost

T = int(input())
for _ in range(T):
    N, m, t = map(int, input().split())  # 교차로, 도로, 목적지 개수
    s, g, h = map(int, input().split())  # 예술가의 출발지, 예술가들은 g와 h 교차로 사이 도로를 지나갔다.
    graph = [[] for _ in range(N + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split()) # a와 b 사이 길에 가중치 d만큼의 양방향 도로
        if (a == g and b == h) or (a == h and b == g):
            graph[a].append([d - 0.1, b])
            graph[b].append([d - 0.1, a])
        else:
            graph[a].append((d, b))
            graph[b].append((d, a))

    destination = [int(input()) for _ in range(t)]
    answer = []
    solution = dijkstra(s)
    for i in destination:
        if solution[i] != float('inf') and type(solution[i]) == float:
            answer.append(i)
    print(*sorted(answer))
