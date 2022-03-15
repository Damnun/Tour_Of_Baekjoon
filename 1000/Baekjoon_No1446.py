n, d = map(int, input().split())
graph = [[] for _ in range(10001)]
for _ in range(n):
    start, end, value = map(int, input().split())
    graph[start].append((end, value))
distance = [i for i in range(d + 1)]

for i in range(d + 1):
    if i != 0:
        distance[i] = min(distance[i], distance[i - 1] + 1)
    for e, w in graph[i]:
        if e <= d and distance[e] > w + distance[i]:
            distance[e] = w + distance[i]
print(distance[d])
