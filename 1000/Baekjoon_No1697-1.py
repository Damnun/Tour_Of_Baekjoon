from collections import deque

n, k = map(int, input().split())
visited = [False] * (200001)
visited[n] = True

dist = [-1] * (200001)
dist[n] = 0

queue = deque()
queue.append(n)
while queue:
    x = queue.popleft()
    for i in [x - 1, x + 1, x * 2]:
        if 0 <= i <= 200000 and visited[i] == False:
            visited[i] = True
            dist[i] = dist[x] + 1
            queue.append(i)
print(dist[k])
