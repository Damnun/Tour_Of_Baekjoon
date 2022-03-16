import heapq
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
cost = [float('inf')] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())
cost[start] = 0

queue = []
heapq.heappush(queue, (cost[start], start))

near = [start] * (n + 1)

while queue:
    weight, node = heapq.heappop(queue)
    if cost[node] < weight:
        continue
    for w, n in graph[node]:
        if w + weight < cost[n]:
            cost[n] = w + weight
            near[n] = node
            heapq.heappush(queue, (cost[n], n))


ans = []
tmp = end
while tmp != start:
    ans.append(str(tmp))
    tmp = near[tmp]

ans.append(str(start))
ans.reverse()

print(cost[end])
print(len(ans))
print(" ".join(ans))
